import numpy as np
import matplotlib.pyplot as plt

def adaboost(X, y, num_steps):
    """
    Trains an AdaBoost classifier

    :param X:                   training data containing feature points in columns, np array (d, n)
                                    d - number of weak classifiers
                                    n - number of data
    :param y:                   vector with labels (-1, 1) for feature points in X, np array (n, )
    :param num_steps:           maximum number of iterations

    :return strong_classifier:  dict with fields:
        - strong_classifier['wc'] - weak classifiers (see docstring of find_best_weak), np array (n_wc, )
        - strong_classifier['alpha'] - weak classifier coefficients, np array (n_wc, )
    :return wc_errors:          error of the best weak classifier in each iteration, np array (n_wc, )
    :return upper_bound:        upper bound on the training error in each iteration, np array (n_wc, )
    """
    D = np.ones(y.shape)
    D[y==1] = 0.5/len(np.where(y==1)[0])
    D[y==-1] = 0.5/len(np.where(y==-1)[0])
    strong_classifier, wc_errors, upper_bound = {'wc': np.array([]), "alpha": np.array([])}, np.array([]), np.array([])
    for i in range(num_steps):
        h, err = find_best_weak(X,y, D)
        strong_classifier['wc'] = np.append(strong_classifier['wc'], h)
        strong_classifier['alpha'] = np.append(strong_classifier['alpha'],0.5*np.log((1-err)/err))
        classif = np.sign(h['parity']*(X[h['idx'], :] - h['theta']))
        D[y==classif] *= np.sqrt(err/(1-err))
        D[y!=classif] *= np.sqrt((1-err)/err)
        Z = 2*np.sqrt((1-err)*err)
        if len(upper_bound) == 0:
            upper_bound = np.append(upper_bound, Z)
        else:
            upper_bound = np.append(upper_bound, upper_bound[-1]*Z)
        D = D/Z
        wc_errors = np.append(wc_errors, err)
        if err>=0.5:
            break
    return strong_classifier, wc_errors, upper_bound


def adaboost_classify(strong_classifier, X):
    """ Classifies data X with a strong classifier

    :param strong_classifier:   classifier returned by adaboost (see docstring of adaboost)
    :param X:                   testing data containing feature points in columns, np array (d, n)
                                    d - number of weak classifiers
                                    n - number of data
    :return classif:            classification labels (values -1, 1), np array (n, )
    """
    classifiers = strong_classifier['wc']
    errors = []
    f = np.zeros(X.shape[1])
    i = 0
    for classifier in classifiers:
        f += strong_classifier['alpha'][i]*np.sign(classifier['parity']*(X[classifier['idx'], :]-classifier['theta']))
        classif = np.sign(f)
        i+=1
    return classif


def compute_error(strong_classifier, X, y):
    """
    Computes the error on data X for all lengths of the given strong classifier

    :param strong_classifier:   classifier returned by adaboost - with T weak classifiers (see docstring of adaboost)
    :param X:                   testing data containing feature points in columns, np array (d, n)
                                    d - number of weak classifiers
                                    n - number of data
    :param y:                   testing labels (-1 or 1), np array (n, )
    :return errors:             errors of the strong classifier for all lengths from 1 to T, np array (T, )
    """
    classifiers = strong_classifier['wc']
    errors = []
    f = np.zeros(y.shape)
    i = 0
    for classifier in classifiers:
        f += strong_classifier['alpha'][i]*np.sign(classifier['parity']*(X[classifier['idx'], :]-classifier['theta']))
        classif = np.sign(f)
        # print(strong_classifier['alpha'][i]*classifier['parity']*(X[classifier['idx'], :]-classifier['theta']))
        errors.append(np.mean(classif!=y))
        i+=1
    return np.array(errors)



################################################################################
#####                                                                      #####
#####             Below this line are already prepared methods             #####
#####                                                                      #####
################################################################################


def find_best_weak(X, y, D):
    """Finds best weak classifier

    Searches over all weak classifiers and their parametrisation
    (threshold and parity) for the weak classifier with lowest
    weighted classification error.

    The weak classifier realises following classification function:
        sign(parity * (x - theta))

    :param X:           training data containing feature points in columns, np array (d, n)
                            d - number of weak classifiers
                            n - number of data
    :param y:           vector with labels (-1, 1) for feature points in X, np array (n, )
    :param D:           training data weights, np array (n, )

    :return wc:         dict representing weak classifier with following fields:
        - wc['idx'] - index of the selected weak classifier, scalar
        - wc['theta'] - the classification threshold, scalar
        - wc['parity'] - the classification parity, scalar
    :return wc_error:   the weighted error of the selected weak classifier
    """
    assert X.ndim == 2
    assert y.ndim == 1
    assert y.size == X.shape[1]
    assert D.ndim == 1
    assert D.size == X.shape[1]

    N_wc, N = X.shape
    best_err = np.inf
    wc = {}

    for i in range(N_wc):
        weak_X = X[i, :] # weak classifier evaluated on all data

        thresholds = np.unique(weak_X)
        assert thresholds.ndim == 1

        if thresholds.size > 1:
            thresholds = (thresholds[:-1] + thresholds[1:]) / 2.
        else:
            thresholds = np.array([+1, -1] + thresholds[0])
        assert thresholds.ndim == 1

        K = thresholds.size

        classif = np.sign(np.reshape(weak_X, (N, 1)) - np.reshape(thresholds, (1, K)))
        assert classif.ndim == 2
        assert classif.shape[0] == N
        assert classif.shape[1] == K

        # Broadcast
        column_D = np.reshape(D, (N, 1))
        column_y = np.reshape(y, (N, 1))
        err_pos = np.sum(column_D * (classif != column_y), axis=0)
        err_neg = np.sum(column_D * (-classif != column_y), axis=0)

        assert err_pos.ndim == 1
        assert err_pos.shape[0] == K
        assert err_neg.ndim == 1
        assert err_neg.shape[0] == K

        min_pos_idx = np.argmin(err_pos)
        min_pos_err = err_pos[min_pos_idx]

        min_neg_idx = np.argmin(err_neg)
        min_neg_err = err_neg[min_neg_idx]

        if min_pos_err < min_neg_err:
            err = min_pos_err
            parity = 1
            theta = thresholds[min_pos_idx]
        else:
            err = min_neg_err
            parity = -1
            theta = thresholds[min_neg_idx]

        if err < best_err:
            wc['idx'] = i
            wc['theta'] = theta
            wc['parity'] = parity
            best_err = err
    return wc, best_err


def show_classification(test_images, labels):
    """
    show_classification(test_images, labels, letters)

    create montages of images according to estimated labels

    :param test_images:     np array (h, w, n)
    :param labels:          labels for input images np array (n,)
    """

    def montage(images, colormap='gray'):
        """
        Show images in grid.

        :param images:      np array (h, w, n)
        :param colormap:    numpy colormap
        """
        h, w, count = np.shape(images)
        h_sq = np.int(np.ceil(np.sqrt(count)))
        w_sq = h_sq
        im_matrix = np.zeros((h_sq * h, w_sq * w))

        image_id = 0
        for j in range(h_sq):
            for k in range(w_sq):
                if image_id >= count:
                    break
                slice_w = j * h
                slice_h = k * w
                im_matrix[slice_h:slice_h + w, slice_w:slice_w + h] = images[:, :, image_id]
                image_id += 1
        plt.imshow(im_matrix, cmap=colormap)
        plt.axis('off')
        return im_matrix

    imgs = test_images[..., labels == 1]
    subfig = plt.subplot(1, 2, 1)
    montage(imgs)
    plt.title('selected')

    imgs = test_images[..., labels == -1]
    subfig = plt.subplot(1, 2, 2)
    montage(imgs)
    plt.title('others')


def show_classifiers(class_images, classifier):
    """
    :param class_images:  images of a selected number, np array (h, w, n)
    :param classifier:    adaboost classifier
    """
    assert len(class_images.shape) == 3
    mean_image = np.mean(class_images, axis=2)
    mean_image = np.dstack((mean_image, mean_image, mean_image))
    vis = np.reshape(mean_image, (-1, 3))
    max_alpha = np.amax(classifier['alpha'])

    for i, wc in enumerate(classifier['wc']):
        c = classifier['alpha'][i] / float(max_alpha)
        if wc['parity'] == 1:
            color = (c, 0, 0)
        else:
            color = (0, c, 0)
        vis[wc['idx'], :] = color

    vis = np.reshape(vis, mean_image.shape)
    plt.imshow(vis)
    plt.axis('off')

# X = np.array([[1, 1.5, 2.5, 3.0, 3.5, 5, 5.5, 6, 7., 8], [1, 4, 2, 8, 1, 4, 3, 5, 7, 11]])
# y = np.array([1, -1, 1, -1, 1, -1, 1, -1, 1, -1])
# strong_classifier, wc_error, upper_bound = adaboost(X, y, 3)
# # print('strong_classifier: ', strong_classifier, '\nwc_error: ', wc_error, '\nupper_bound: ', upper_bound)
# trn_errors = compute_error(strong_classifier, X, y)
# print('trn_error: ', trn_errors)

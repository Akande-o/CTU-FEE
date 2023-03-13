### IMPORTING THE REQUIRED MODULES
import argparse
from collections import Counter
import csv
import os
from PIL import Image
import numpy as np
import math
import time

## PARSER ##
def setup_arg_parser():
    """
    This function uses the argparse module to help run the parameters from the command line and returns
    an argparse object 
    """
    parser = argparse.ArgumentParser(description='Learn and classify image data.')
    parser.add_argument('train_path', type=str, help='path to the training data directory')
    parser.add_argument('test_path', type=str, help='path to the testing data directory')
    mutex_group = parser.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('-k', type=int, 
                             help='run k-NN classifier (if k is 0 the code may decide about proper K by itself')
    mutex_group.add_argument("-b", 
                             help="run Naive Bayes classifier", action="store_true")
    parser.add_argument("-o", metavar='filepath', 
                        default='classification.dsv',
                        help="path (including the filename) of the output .dsv file with the results")
    return parser

def read_dsv(file_path):
    """
    This function returns a dictionary which corresponds to the training data in the form of file name 
    as the keys and the output as the values
    Parameters:
    file_path - The path to the input dsv file where the training data is saved in a particular format
    """
    train_dict = {} # initialising the dictionary
    with open(file_path) as train_dsv:
        csv_reader = csv.reader(train_dsv)  # reading the dsv file
        for data in list(csv_reader):
            data = data[0]  # since there are no commas we can read the dsv file directly as string 
            data = data.split(":") # splitting the data according to columns
            train_dict[data[0]] = data[1] # setting the keys as file names and output as values
    return train_dict

def Naive_Bayes(train_path, train_dict, test_path):
    """
    This function returns a dictionary of the test data with the image names as keys and the predictions as values
    using the Naive Bayes machine learning algorithm 
    Parameters:
    train_path- The path to the training image data
    train_dict - The dictionary with training images as keys and output as values
    test_path - The path to the testing image data
    Returns:
    test_dict - The dictionary with testing image file names as keys and predictions as values
    """
    N = len(train_dict.keys())    # number of training images
    values = list(set(train_dict.values())) # the classes of the training data output
    freq = Counter(train_dict.values()) # The number of occurences for each class in the training data
    X = []
    probs = []
    test_dict = {}
    ## GETTING THE TRAINING DATA ##
    for train_case in train_dict.keys():
        im = np.array(Image.open(os.path.join(train_path, train_case))).astype(int).flatten()
        im = np.where(im>130, 1, 0) # quantizing the image for easier and more accurate computations
        X.append([im,train_dict[train_case]])
    ### TRAINING THE MODEL WITH THE IMAGE DATA
    ## For each class
    for num in values:
        digit = []
        for i in range(len(im)):
            digit.append(sum(1 for x in X if x[0][i] == 1 and x[1] == num)) # P(X_pixel|class)
        probs.append(digit) # the probability matrix for each pixel provided the class
    
    ### TESTING EACH CASE BASED ON THE TRAINED MODEL
    # For each test case
    for test_case in os.listdir(test_path):
        ## Using Bayes Theorem and the argmax function to find the most likely class prediction
        max_arg = -np.Inf
        solve = None
        if ".dsv" in test_case or ".png" not in test_case: # skipping the dsv file or anything not an image
            continue 
        im2 = np.array(Image.open(os.path.join(test_path, test_case))).astype(int).flatten()
        im2 = np.where(im2>130, 1, 0) # quantized image
        # For each class
        for j in range(len(values)):
            prob = math.log(freq[values[j]]/N) # P(Class)
            for i in range(len(im2)):
                if im2[i] == 1:
                    n = probs[j][i] # checking for the number of possibilities given the training data
                else:
                    n = freq[values[j]] - probs[j][i] # checking for the number of possibilities given the training data
                if n == 0:
                    prob += math.log(1/(N + len(values))) # Laplace smoothing 
                else:
                    prob += math.log(n/N) # P(x[1]|class)* P(x[2|class]) .... P(x[end]|class)
            # argmax()
            if prob > max_arg:
                max_arg = prob
                solve = values[j]
        test_dict[test_case] = solve
    
    return test_dict
        




def KNN(train_path,train_dict, test_path, k):
    """
    This function returns a dictionary of the test data with the image names as keys and the predictions as values
    using the K Nearest Neighbors learning algorithm 
    Parameters:
    train_path- The path to the training image data
    train_dict - The dictionary with training images as keys and output as values
    test_path - The path to the testing image data
    Returns:
    test_dict - The dictionary with testing image file names as keys and predictions as values
    """
    test_dict = {}
    # for each test image
    for test_case in os.listdir(test_path):
        if ".dsv" in test_case or ".png" not in test_case: # skipping the dsv file
            continue
        distances = []  
        neighbors = []
        im1 = np.array(Image.open(os.path.join(test_path, test_case))).astype(int).flatten() # test
        for train_case in train_dict.keys():
            im2 = np.array(Image.open(os.path.join(train_path, train_case))).astype(int).flatten() # train image
            # finding the distance between the test image and each train image
            diff = im1 - im2  
            d2 = np.linalg.norm(diff)
            distances.append((train_case, d2))
        distances.sort(key = lambda x: x[1]) # sorting in ascending order
        # print(distances)
        for i in range(k):
            neighbors.append(train_dict[distances[i][0]])  # getting the k smallest values
        # print(neighbors)
        point_class = Counter(neighbors)
        # assigning the closest and most frequent training image value
        if len(point_class.keys()) < k:
            points = sorted(point_class.items(), key = lambda x:x[1], reverse=True)[0]
            test_dict[test_case] = points[0]  
            
        else:
            test_dict[test_case] = list(point_class.keys())[0]
        # print(test_case, test_dict[test_case])
    return test_dict


        



def main():
    parser = setup_arg_parser()
    args = parser.parse_args()
    
    print('Training data directory:', args.train_path)
    print('Testing data directory:', args.test_path)
    print('Output file:', args.o)
    train_dict = read_dsv(os.path.join(args.train_path, "truth.dsv"))
    
    if args.k is not None:
        print(f"Running k-NN classifier with k={args.k}")
        output_dict = KNN(args.train_path,train_dict, args.test_path, args.k)
        # TODO Train and test the k-NN classifier
    elif args.k == 0:
        print(f"Running k-NN classifier with k=3")
        output_dict = KNN(args.train_path,train_dict, args.test_path, 3)
    elif args.b:
        print("Running Naive Bayes classifier")
        output_dict = Naive_Bayes(args.train_path,train_dict, args.test_path)
    #     # TODO Train and test the Naive Bayes classifier
    with open(os.path.join(args.test_path, args.o), "w") as csv_output:
        writer = csv.writer(csv_output, delimiter=":")
        writer.writerows(output_dict.items())
        
if __name__ == "__main__":
    main()
    

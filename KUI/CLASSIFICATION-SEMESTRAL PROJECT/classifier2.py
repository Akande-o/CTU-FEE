import argparse
from collections import Counter
import csv
import os
from PIL import Image
import numpy as np
import math
import time
 
 
def setup_arg_parser():
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
    train_dict = {}
    with open(file_path) as train_dsv:
        csv_reader = csv.reader(train_dsv)
        for data in list(csv_reader):
            data = data[0]
            data = data.split(":")
            train_dict[data[0]] = data[1]
    return train_dict
 
def Naive_Bayes(train_path, train_dict, test_path):
    t0 = time.time()
    N = len(train_dict.keys())
    values = set(train_dict.values())
    freq = Counter(train_dict.values())
    X = []
    test_dict = {}
    for train_case in train_dict.keys():
        im = np.array(Image.open(os.path.join(train_path, train_case))).astype(int).flatten()
        im = np.where(im>100, 1, 0)
        X.append([im,train_dict[train_case]] )
    t1 = time.time()
    for test_case in os.listdir(test_path):
        max_arg = -np.Inf
        solve = None
        if ".dsv" in test_case or ".png" not in test_case:
            continue
        im2 = np.array(Image.open(os.path.join(test_path, test_case))).astype(int).flatten()
        im2 = np.where(im2>100, 1, 0)
        for num in values:
            prob = math.log(freq[num]/N)
            for i in range(len(im2)):
                n = sum(1 for x in X if x[0][i] == im2[i] and x[1] == num)
                if n == 0:
                    print("we have success")
                    prob += math.log(1/(N + len(values)))
                else:
                    prob += math.log(n/N)
            if prob > max_arg:
                max_arg = prob
                solve = num
            # print(prob)
        test_dict[test_case] = solve
        print(test_case, solve)
        t2 = time.time()
        # print(t2-t1)
        # print(t1-t0)
    return test_dict
         
 
 
 
 
def KNN(train_path,train_dict, test_path, k):
    test_dict = {}
    for test_case in os.listdir(test_path):
        if ".dsv" in test_case or ".png" not in test_case:
            continue
        distances = []
        neighbors = []
        for train_case in train_dict.keys():
            im1 = np.array(Image.open(os.path.join(test_path, test_case))).astype(int).flatten()
            im2 = np.array(Image.open(os.path.join(train_path, train_case))).astype(int).flatten()
            diff = im1 - im2
            # d1 = np.sqrt(np.sum(np.square(diff)))
            d2 = np.linalg.norm(diff)
            distances.append((train_case, d2))
        distances.sort(key = lambda x: x[1])
        # print(distances)
        for i in range(k):
            neighbors.append(train_dict[distances[i][0]])
        # print(neighbors)
        point_class = Counter(neighbors)
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
    
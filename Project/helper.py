from project import submission as sub
import pickle
import time
import numpy as np


if __name__ == '__main__':
    # # How to run your implementation for Part 1
    # with open('./toy_example/Data_File', 'rb') as f:
    #     data = pickle.load(f, encoding='bytes')
    #
    # with open('./toy_example/Centroids_File', 'rb') as f:
    #     centroids = pickle.load(f, encoding='bytes')
    #
    # start = time.time()
    # codebooks, codes = sub.pq(data, P=2, init_centroids=centroids, max_iter=20)
    # end = time.time()
    # time_cost_1 = end - start
    #
    # # How to run your implementation for Part 2
    # # with open('./toy_example/Query_File', 'rb') as f:
    # #     queries = pickle.load(f, encoding='bytes')
    #
    # start = time.time()
    # candidates = sub.query(queries, codebooks, codes, T=10)
    # end = time.time()
    # time_cost_2 = end - start
    #
    # # output for part 2.
    # print(candidates)
    # print(time_cost_2)

    # number of data points
    N = 1000
    # number of features
    M = 128
    # number of codewords for each codebook
    K = 256
    # number of blocks
    P = 1
    # number of queries
    Q = 1
    # set seed
    np.random.seed(0)

    for i in range(5):
        P = int(2 ** i)
        print('P = {}'.format(P))

        my_Data_file = 10 * np.random.random_sample((N, M))
        my_Centroids_File = 10 * np.random.random_sample((K, M))
        my_Centroids_File = np.array(np.hsplit(my_Centroids_File, P))
        start = time.time()
        codebooks, codes = sub.pq(my_Data_file, P=P, init_centroids=my_Centroids_File, max_iter=20)
        end = time.time()
        time_cost_1 = end - start
        print(time_cost_1)

        my_Queries = 10 * np.random.random_sample((Q, M))
        start = time.time()
        candidates = sub.query(my_Queries, codebooks, codes, T=10)
        print(candidates)
        end = time.time()
        time_cost_2 = end - start

        # output for part 2.
        print(time_cost_2)
        print()

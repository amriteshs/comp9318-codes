import numpy as np
from scipy.spatial.distance import cdist
from heapq import heappush, heappop


def pq(data, P, init_centroids, max_iter):
    N = data.shape[0]
    dim = init_centroids.shape[2]

    codebooks = np.array(init_centroids, dtype=np.float32)
    codes = np.empty((N, P), dtype=np.uint8)

    for itr in range(max_iter):
        temp = np.array(codebooks, copy=True)

        for i in range(P):
            subvec = data[:, i * dim:(i + 1) * dim]
            codes[:, i] = np.apply_along_axis(np.argmin, 1, cdist(subvec, codebooks[i], metric='cityblock'))

            valid_centroids = np.unique(codes[:, i])

            for j in valid_centroids:
                codebooks[i, j] = np.median(np.array([subvec[t] for t in np.where(codes[:, i] == j)]), axis=1)[0]

        if np.array_equal(temp, codebooks):
            break

    for i in range(P):
        subvec = data[:, i * dim:(i + 1) * dim]
        codes[:, i] = np.apply_along_axis(np.argmin, 1, cdist(subvec, codebooks[i], metric='cityblock'))

    return codebooks, codes

def query(queries, codebooks, codes, T):
    candidates = []
    P = codebooks.shape[0]
    Q = queries.shape[0]

    for i in range(Q):
        idx_candidates = {}

        idx = 0
        for j in codes:
            key = tuple([c for c in j])

            if key not in idx_candidates:
                idx_candidates[key] = [idx]
            else:
                idx_candidates[key] += [idx]

            idx += 1

        q = np.array(np.split(np.array([queries[i]]), P, axis=1))
        distances = np.array([cdist(q[j], codebooks[j], metric='cityblock')[0] for j in range(P)])

        heap = []
        idx_distances = {}
        for key, val in idx_candidates.items():
            idx_distances[key] = 0
            ctr = 0
            for j in key:
                idx_distances[key] += distances[ctr][j]
                ctr += 1

            heappush(heap, (idx_distances[key], key))

        q_candidates = set()
        while len(q_candidates) < T:
            heap_item = heappop(heap)
            q_candidates.update(idx_candidates[heap_item[1]])

        candidates.append(q_candidates)

    return candidates

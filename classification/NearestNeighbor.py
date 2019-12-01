from scipy.spatial import distance
import Image
import numpy as np
import NearestNeighborTracker
from collections import Counter

def nearest_neighbor_face_training(data, predict, k = 3):
    pd =[]
    for image in predict:
        distances = []
        for image2 in data:
            euclidean_distance = np.linalg.norm(image2.class_features-image.class_features)
            distances.append(NearestNeighborTracker.NearestNeighborTracker(image.class_label,euclidean_distance))

        distances.sort(key=lambda x: x.class_distance, reverse=True)
        vote_array = [0,0,0]
        vote_array[0] = distances[0].class_label
        vote_array[1] = distances[1].class_label
        vote_array[2] = distances[2].class_label
        pd.append(most_frequent(vote_array))
    return pd

# taken from https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]





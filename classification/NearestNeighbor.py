import Image
import numpy as np
import NearestNeighborTracker
from collections import Counter

def nearest_neighbor(TestingData, trainingData):
    pd =[]
    for image in trainingData:
        distances = []
        for image2 in TestingData:
            distance = np.linalg.norm(image2.class_features-image.class_features)
            distances.append(NearestNeighborTracker.NearestNeighborTracker(image2.class_label,distance))
        distances.sort(key=lambda x: x.class_distance, reverse=False)

        vote_array = [0,0,0,0,0,0,0,0,0,0,0]
        vote_array[0] = distances[0].class_label
        vote_array[1] = distances[1].class_label
        vote_array[2] = distances[2].class_label
        vote_array[3] = distances[3].class_label
        vote_array[4] = distances[4].class_label
        vote_array[5] = distances[5].class_label
        vote_array[6] = distances[6].class_label
        vote_array[7] = distances[7].class_label
        vote_array[8] = distances[8].class_label
        vote_result = most_frequent(vote_array)
        pd.append(vote_result)

    return pd

# taken from https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]





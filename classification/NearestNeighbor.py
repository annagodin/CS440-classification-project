import Image
import numpy as np
import NearestNeighborTracker
from collections import Counter

def nearest_neighbor(data, predict):
    pd =[]
    for image in predict:
        distances = []
        for image2 in data:
            distance = np.linalg.norm(image2.class_features-image.class_features)
            distances.append(NearestNeighborTracker.NearestNeighborTracker(image2.class_label,distance))
        distances.sort(key=lambda x: x.class_distance, reverse=False)

        vote_array = [0,0,0]
        vote_array[0] = distances[0].class_label
        vote_array[1] = distances[1].class_label
        vote_array[2] = distances[2].class_label
        vote_result = Counter(vote_array).most_common(1)[0][0]
        pd.append(vote_result)

    return pd

# taken from https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]





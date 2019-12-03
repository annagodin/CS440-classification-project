import decimal

import Image
import numpy as geek
import PercentageTracker
import random


def perceptron_face_training(face_image_data_training, face_image_data_testing, feature_size):
    weights = []  # 0....100, weight[0] is the bias
    num_right = 0
    num_rounds = 0
    percent_accuracy = 0
    for i in range(0, feature_size + 1):  # assigning random weights
        weights.append(decimal.Decimal(random.randrange(-50, 50)) / 100)
    # print weights
    while percent_accuracy < .85:
        for image in face_image_data_training:
            # image = face_image_data_training[0]
            fx = 0
            for j in range(1, feature_size + 1):  # 1-100
                # print str(image.class_features[j - 1]) + ", " + str(weights[j]),
                fx += weights[j] * image.class_features[j - 1]  # calculate f(x)

            # print "\n"
            # print fx
            # print image.class_label
            if fx < 0 and image.class_label == '0':
                # print "correct!"
                num_right += 1
            elif fx >= 0 and image.class_label == '1':
                # print "correct!"
                num_right += 1
            elif fx < 0 and image.class_label == '1':
                # print "wrong prediction"
                for i in range(1, feature_size + 1):
                    weights[i] += image.class_features[i - 1]
                weights[0] += 1
                # print weights
            elif fx >= 0 and image.class_label == '0':
                # print "wrong prediction"
                for i in range(1, feature_size + 1):
                    weights[i] -= image.class_features[i - 1]
                weights[0] -= 1
                # print weights
            num_rounds += 1
        percent_accuracy = float(num_right) / num_rounds
        # print "percent accuracy: " + str(float(num_right) / num_rounds)
    # print num_rounds
    # print num_right

    # -----------------------------------------------------------------------------------------#
    # TESTING TIME#
    # -----------------------------------------------------------------------------------------#

    guess_array = []
    for image in face_image_data_testing:
        fx = 0
        for j in range(1, feature_size + 1):  # 1-100
            # print str(image.class_features[j - 1]) + ", " + str(weights[j]),
            fx += weights[j] * image.class_features[j - 1]  # calculate f(x)
        if fx < 0:
            guess_array.append('0')
        else:
            guess_array.append('1')

    return guess_array


def perceptron_digit_training(digit_image_data_training, digit_image_data_testing, feature_size):
    return 0

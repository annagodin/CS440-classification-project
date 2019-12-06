import Image
import numpy as geek
import PercentageTracker


def naive_bayes_face_training(face_image_data_training, face_image_data_testing, feature_size):
    max = 0
    total_num_faces = 0
    total_num_not_face = 0

    for image in face_image_data_training:  # 5000
        if (image.class_label == '0'):
            total_num_not_face += 1
        elif (image.class_label == '1'):
            total_num_faces += 1
        for class_feature in image.class_features:
            if (class_feature > max):
                max = class_feature

    bayes_matrix_face = geek.empty([feature_size, max + 1])
    bayes_matrix_not_face = geek.empty([feature_size, max + 1])
    bayes_matrix_not_face.fill(0.001)
    bayes_matrix_face.fill(0.001)

    for image in face_image_data_training:
        for i in range(feature_size):  # i = feature Num
            for j in range(max + 1):  # j = pixel range
                if (image.class_label == '0'):  # not face
                    if (image.class_features[i] == j):
                        bayes_matrix_not_face[i][j] += 1

                elif (image.class_label == '1'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_face[i][j] += 1

    for i in range(feature_size):
        for j in range(max + 1):
            bayes_matrix_not_face[i][j] = (bayes_matrix_not_face[i][j] / total_num_not_face)
            bayes_matrix_face[i][j] = (bayes_matrix_face[i][j] / total_num_faces)

    # -------------------------------------------------------------------------------------------Testing begins

    guess_array = []
    for image in face_image_data_testing:  # 5000
        face_tally = 1
        not_face_tally = 1
        index = 0
        for class_feature in image.class_features:
            if class_feature <= max:
                face_tally = (face_tally * bayes_matrix_face[index][class_feature])
                not_face_tally = (not_face_tally * bayes_matrix_not_face[index][class_feature])
            else:
                face_tally = face_tally*0.001
                not_face_tally = not_face_tally*0.001
            index += 1
        if face_tally >= not_face_tally:
            guess_array.append('1')
        if face_tally < not_face_tally:
            guess_array.append('0')

    return guess_array


def naive_bayes_digit_training(digit_image_data_training, digit_image_data_testing, feature_size):
    max = 0
    digit_data_total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 to 9
    for image in digit_image_data_training:  # 5000
        if (image.class_label == '0'):
            digit_data_total[0] += 1

        elif (image.class_label == '1'):
            digit_data_total[1] += 1

        elif (image.class_label == '2'):
            digit_data_total[2] += 1

        elif (image.class_label == '3'):
            digit_data_total[3] += 1

        elif (image.class_label == '4'):
            digit_data_total[4] += 1

        elif (image.class_label == '5'):
            digit_data_total[5] += 1

        elif (image.class_label == '6'):
            digit_data_total[6] += 1

        elif (image.class_label == '7'):
            digit_data_total[7] += 1

        elif (image.class_label == '8'):
            digit_data_total[8] += 1

        elif (image.class_label == '9'):
            digit_data_total[9] += 1

        for class_feature in image.class_features:
            if (class_feature > max):
                max = class_feature

    bayes_matrix_zero = geek.empty([feature_size, max + 1])
    bayes_matrix_one = geek.empty([feature_size, max + 1])
    bayes_matrix_two = geek.empty([feature_size, max + 1])
    bayes_matrix_three = geek.empty([feature_size, max + 1])
    bayes_matrix_four = geek.empty([feature_size, max + 1])
    bayes_matrix_five = geek.empty([feature_size, max + 1])
    bayes_matrix_six = geek.empty([feature_size, max + 1])
    bayes_matrix_seven = geek.empty([feature_size, max + 1])
    bayes_matrix_eight = geek.empty([feature_size, max + 1])
    bayes_matrix_nine = geek.empty([feature_size, max + 1])
    bayes_matrix_zero.fill(0.001)
    bayes_matrix_one.fill(0.001)
    bayes_matrix_two.fill(0.001)
    bayes_matrix_three.fill(0.001)
    bayes_matrix_four.fill(0.001)
    bayes_matrix_five.fill(0.001)
    bayes_matrix_six.fill(0.001)
    bayes_matrix_seven.fill(0.001)
    bayes_matrix_eight.fill(0.001)
    bayes_matrix_nine.fill(0.001)

    for image in digit_image_data_training:
        for i in range(feature_size):  # i = feature Num
            for j in range(max + 1):  # j = pixel range
                if (image.class_label == '0'):  # not face
                    if (image.class_features[i] == j):
                        bayes_matrix_zero[i][j] += 1

                elif (image.class_label == '1'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_one[i][j] += 1

                elif (image.class_label == '2'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_two[i][j] += 1

                elif (image.class_label == '3'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_three[i][j] += 1

                elif (image.class_label == '4'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_four[i][j] += 1

                elif (image.class_label == '5'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_five[i][j] += 1

                elif (image.class_label == '6'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_six[i][j] += 1

                elif (image.class_label == '7'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_seven[i][j] += 1

                elif (image.class_label == '8'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_eight[i][j] += 1

                elif (image.class_label == '9'):  # is face
                    if (image.class_features[i] == j):
                        bayes_matrix_nine[i][j] += 1

    for i in range(feature_size):
        for j in range(max + 1):
            bayes_matrix_zero[i][j] = (bayes_matrix_zero[i][j] / digit_data_total[0])
            bayes_matrix_one[i][j] = (bayes_matrix_one[i][j] / digit_data_total[1])
            bayes_matrix_two[i][j] = (bayes_matrix_two[i][j] / digit_data_total[2])
            bayes_matrix_three[i][j] = (bayes_matrix_three[i][j] / digit_data_total[3])
            bayes_matrix_four[i][j] = (bayes_matrix_four[i][j] / digit_data_total[4])
            bayes_matrix_five[i][j] = (bayes_matrix_five[i][j] / digit_data_total[5])
            bayes_matrix_six[i][j] = (bayes_matrix_six[i][j] / digit_data_total[6])
            bayes_matrix_seven[i][j] = (bayes_matrix_seven[i][j] / digit_data_total[7])
            bayes_matrix_eight[i][j] = (bayes_matrix_eight[i][j] / digit_data_total[8])
            bayes_matrix_nine[i][j] = (bayes_matrix_nine[i][j] / digit_data_total[9])

    # -------------------------------------------------------------------------------------------Testing begins

    guess_array = []
    for image in digit_image_data_testing:  # 5000
        num_tally = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        index = 0
        percent_array = []
        for class_feature in image.class_features:
            num_tally[0] = (num_tally[0] * bayes_matrix_zero[index][class_feature])
            num_tally[1] = (num_tally[1] * bayes_matrix_one[index][class_feature])
            num_tally[2] = (num_tally[2] * bayes_matrix_two[index][class_feature])
            num_tally[3] = (num_tally[3] * bayes_matrix_three[index][class_feature])
            num_tally[4] = (num_tally[4] * bayes_matrix_four[index][class_feature])
            num_tally[5] = (num_tally[5] * bayes_matrix_five[index][class_feature])
            num_tally[6] = (num_tally[6] * bayes_matrix_six[index][class_feature])
            num_tally[7] = (num_tally[7] * bayes_matrix_seven[index][class_feature])
            num_tally[8] = (num_tally[8] * bayes_matrix_eight[index][class_feature])
            num_tally[9] = (num_tally[9] * bayes_matrix_nine[index][class_feature])
            index += 1

        percent_array.append(PercentageTracker.PercentageTracker('0', num_tally[0]))
        percent_array.append(PercentageTracker.PercentageTracker('1', num_tally[1]))
        percent_array.append(PercentageTracker.PercentageTracker('2', num_tally[2]))
        percent_array.append(PercentageTracker.PercentageTracker('3', num_tally[3]))
        percent_array.append(PercentageTracker.PercentageTracker('4', num_tally[4]))
        percent_array.append(PercentageTracker.PercentageTracker('5', num_tally[5]))
        percent_array.append(PercentageTracker.PercentageTracker('6', num_tally[6]))
        percent_array.append(PercentageTracker.PercentageTracker('7', num_tally[7]))
        percent_array.append(PercentageTracker.PercentageTracker('8', num_tally[8]))
        percent_array.append(PercentageTracker.PercentageTracker('9', num_tally[9]))

        percent_array.sort(key=lambda x: x.class_percent, reverse=True)
        guess_array.append(percent_array[0].class_label)

    return guess_array

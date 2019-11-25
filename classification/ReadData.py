import random
import Image
import Bayes
import numpy as geek
# import numpy as np


def read_data(file_name, type):
    if type == "digit":
        image_size = 28
    else:
        image_size = 70

    numbers = []
    with open(file_name) as fp:
        line = fp.readline()
        count_rows = 0
        image = []
        while line:
            row = []
            for c in line:
                if c == ' ':
                    row.append('0')
                else:
                    row.append('1')
            row.pop(len(row) - 1)
            image.append(row)

            count_rows += 1
            if count_rows == image_size:
                count_rows = 0
                numbers.append(image)
                # for irow in image:
                #     print(irow)
                # print("\n")
                image = []
            line = fp.readline()
    return numbers


def read_labels(file_name):
    labels = []
    with open(file_name) as fp:
        line = fp.readline()
        # print(line)
        while line:
            line = line[:-1]
            labels.append(line)
            line = fp.readline()
    return labels


def extract_features(data, data_labels):
    image_info = []
    index = 0
    count = 0
    for image in data:
        features = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for row in range(len(image)):
            r = (len(image) / 3)

            for col in range(len(image[row])):
                c = (len(image[row]) / 3)

                if image[row][col] == '1':  # if black pixel

                    if row <= r and col <= c:  # Quadrant 1
                        features[0] += 1

                    elif r < row <= (2 * r) and col <= c:  # Quadrant 2
                        features[1] += 1

                    elif row > (2 * r) and col <= c:  # Quadrant 3
                        features[2] += 1

                    elif row <= r and c < col <= (2 * c):  # Quadrant 4
                        features[3] += 1

                    elif r < row < (2 * r) and c < col <= (2 * c):  # Quadrant 5
                        features[4] += 1

                    elif row > (2 * r) and c < col <= (2 * c):  # Quadrant 6
                        features[5] += 1

                    elif row <= r and col > (2 * c):  # Quadrant 7
                        features[6] += 1

                    elif r < row <= (2 * r) and col > (2 * c):  # Quadrant 8
                        features[7] += 1

                    elif row > (2 * r) and col > (2 * c):  # Quadrant 9
                        features[8] += 1

                    else:
                        continue

        image_info.append(Image.Image(data_labels[index], features))
        index = index + 1
    return image_info

# main
train_digit_image = "data/digitdata/trainingimages"
train_face_image = "data/facedata/facedatatrain"

train_digit_label = "data/digitdata/traininglabels"
train_face_label = "data/facedata/facedatatrainlabels"

train_digit_image_list = read_data(train_digit_image, "digit")
train_face_image_list = read_data(train_face_image, "face")
#
train_digit_labels_list = read_labels(train_digit_label)
train_face_labels_list = read_labels(train_face_label)

image_info_list = extract_features(train_digit_image_list, train_digit_labels_list)
#print image_info_list[0].class_features

face_info_list = extract_features(train_face_image_list, train_face_labels_list )
#print face_info_list[6].class_label

guess = []
guess = Bayes.naive_bayes_face_training(face_info_list,face_info_list,9)


#count = 0
#for i in range(len(guess)):
 #   if(guess[i] == train_face_labels_list[i]):
  #      count +=1

#print count
#print len(guess)


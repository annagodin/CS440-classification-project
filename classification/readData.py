import random
import statistics


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


# ------ Debug -------
# for image in train_digit_image_list:
#     for row in image:
#         for i in row:
#             print(i + " ", end='')
#         print("\n")
#     print("\n")

print(len(train_digit_image_list)) #how many digit images
print(len(train_digit_image_list[0])) #number of rows in an image
print(len(train_digit_image_list[0][0])) #number of columns in an image
print()
print(len(train_face_image_list)) #how many face images
print(len(train_face_image_list[0])) #number of rows in an image
print(len(train_face_image_list[0][0])) #number of columns in an image
print()
print(len(train_digit_labels_list)) #lengs of label array digits
print(len(train_face_labels_list)) #length of label array faces
# length_digit_train = len(train_digit_image_list)
# print(length_digit_train)
# print(length_digit_train/28)

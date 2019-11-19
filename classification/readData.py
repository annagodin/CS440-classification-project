import random
import statistics


def read_data(file_name):
    numbers = []
    with open(file_name) as fp:
        line = fp.readline()
        count_rows = 0
        while line:
            row = []
            for c in line:
                if c == ' ':
                    row.append(0)
                else:
                    row.append(1)
            row.pop(len(row) - 1)
            count_rows += 1
            numbers.append(row)
            line = fp.readline()
    return numbers


def read_labels(file_name):
    labels = []
    with open(file_name) as fp:
        line = fp.readline()
        # print(line)
        while line:
            line=line[:-1]
            labels.append(line)
            line = fp.readline()
    return labels


# main
train_digit_image = "data/digitdata/trainingimages"
train_face_image = "data/facedata/facedatatrain"

train_digit_label = "data/digitdata/traininglabels"
train_face_label = "data/facedata/facedatatrainlabels"

train_digit_image_list = read_data(train_digit_image)
train_face_image_list = read_data(train_face_image)

train_digit_labels_list = read_labels(train_digit_label)
train_face_labels_list = read_labels(train_face_label)




import Image
import numpy as geek

def naive_bayes_face_training(face_image_data_training, face_image_data_testing,feature_size):
    max = 0
    total_num_faces = 0
    total_num_not_face = 0

    for image in face_image_data_training: #5000
        if(image.class_label == '0'):
            total_num_not_face +=1
        elif(image.class_label == '1'):
            total_num_faces+=1
        for class_feature in image.class_features:
            if(class_feature > max):
                max = class_feature

    bayes_matrix_face = geek.empty([feature_size, max+1])
    bayes_matrix_not_face = geek.empty([feature_size, max+1])
    bayes_matrix_not_face.fill(0)
    bayes_matrix_face.fill(0)

    for image in face_image_data_training:
        for i in range(feature_size): #i = feature Num
            for j in range(max+1): #j = pixel range
                if(image.class_label == '0'): #not face
                    if(image.class_features[i] == j):
                        bayes_matrix_not_face[i][j] +=1

                elif(image.class_label == '1'): #is face
                     if(image.class_features[i] == j):
                        bayes_matrix_face[i][j] +=1

    for i in range(feature_size):
        for j in range(max+1):
                bayes_matrix_not_face[i][j] = (bayes_matrix_not_face[i][j]/total_num_not_face)
                bayes_matrix_face[i][j] = (bayes_matrix_face[i][j]/total_num_faces)


  #-------------------------------------------------------------------------------------------Testing begins

    guess_array = []
    for image in face_image_data_training: #5000
        face_tally = 1
        not_face_tally = 1
        index = 0
        for class_feature in image.class_features:
            face_tally = (face_tally *bayes_matrix_face[index][class_feature])
            not_face_tally = (not_face_tally *bayes_matrix_not_face[index][class_feature])
            index+=1
        if(face_tally>=not_face_tally):
            guess_array.append('1')
        if(face_tally<not_face_tally):
            guess_array.append('0')

    return guess_array

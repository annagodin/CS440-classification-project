# CS440-classification-project
Acknowledgement: This project is based on the one created by Dan Klein and John DeNero that was given as part of the programming assignments of Berkeley’s CS188 course.

In this project, we design three classifiers: a naive Bayes classifier, a perceptron classifier and a K Nearest Neighbors classifier. We test our classifiers on two image data sets: a set of scanned handwritten digit images and a set of face images in which edges have already been detected. Even with simple features, our classifiers are be able to do quite well on these tasks when given enough training data.

Optical character recognition (OCR) is the task of extracting text from image sources. The first data set on which we run our classifiers is a collection of handwritten numerical digits (0-9). This is a very commercially useful technology, similar to the technique used by the US post office to route mail by zip codes. There are systems that can perform with over 99% classification accuracy (see LeNet-5 for an example system in action).

Face detection is the task of localizing faces within video or still images. The faces can be at any location and vary in size. There are many applications for face detection, including human computer interaction and surveillance. We attempt a simplified face detection task in which our system is presented with an image that has been pre-processed by an edge detection algorithm. The task is to determine whether the edge image is a face or not.

Please refer to http://inst.eecs.berkeley.edu/~cs188/sp11/projects/classification/classification.html for a brief description of the Perceptron and Naive Bayes classifiers.

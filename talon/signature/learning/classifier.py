# -*- coding: utf-8 -*-

"""The module's functions could init, train, save and load a classifier.
The classifier could be used to detect if a certain line of the message
body belongs to the signature.
"""

import os
import sys
import numpy

from PyML import SparseDataSet, SVM
from sklearn import svm


def init():
    '''Inits classifier with optimal options.'''
    #return SVM(C=10, optimization='liblinear')
    return svm.LinearSVC(C=10)


def train(classifier, train_data_filename, save_classifier_filename=None):
    '''Trains and saves classifier so that it could be easily loaded later.'''
    data = SparseDataSet(train_data_filename, labelsColumn=-1)
    classifier.train(data)
    if save_classifier_filename:
        classifier.save(save_classifier_filename)
    return classifier


def load(saved_classifier_filename, train_data_filename):
    """Loads saved classifier.

    Classifier should be loaded with the same data it was trained against
    """
    #train_data = SparseDataSet(train_data_filename, labelsColumn=-1)
    train_data = numpy.loadtxt(train_data_filename, delimiter=',', usecols=range(1, 13))
    #classifier_data = numpy.loadtxt(saved_classifier_filename, delimiter=',')

    classifier = init()
    classifier.fit(train_data, numpy.array(xrange(len(train_data))))
    #classifier.load(saved_classifier_filename, train_data)
    return classifier

''' Sentiment Analysis: Based on Andy Bromberg '''
## The imports sections
import re, math, collections, itertools
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
import os
print(os.getcwd())
## Writing the feature evaluator

def evaluate_features (feature_select):
    # reading the pre-labeled inputs and splitting into lines
    posSentences = open('rt-polarity-pos.txt', 'r')
    negSentences = open('rt-polarity-neg.txt', 'r')
    posSentences = re.split(r'\n', posSentences.read())
    negSentences = re.split(r'\n', negSentences.read())
    
    print len(posSentences)
    
    posFeatures = []
    negFeatures = []
    
    #http://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
    #breaks up the sentences into lists of individual words (as selected by the input mechanism) and appends 'pos' or 'neg' after each list
    
    

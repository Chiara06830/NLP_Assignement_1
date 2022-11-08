from nltk import *
from nltk.corpus import *
from nltk.corpus.reader.util import *
import nltk.data
import nltk
import random
from math import *
nltk.download('udhr2')
nltk.download('ppattach')

# ----------------------- TRAIN A CLASSIFIER ----------------------- 
# open two corpus (Universal Declaration of Human Right)
short_en = open(nltk.data.find('corpora/udhr2/eng.txt')).read() # english
short_fr = open(nltk.data.find('corpora/udhr2/fra.txt')).read() # non-english

# prepare list of examples and corresponding labels
documents = []
for r in short_en.split('\n'):
    documents.append((r, "en"))
for r in short_fr.split('\n'):
    documents.append((r, "non_en"))
random.shuffle(documents)

# decide what feature is relevant, here: the whole word
def english_features(word) :
    return {'word': word}

# set of features based on corpus
featuresets = [(english_features(n), lang) for (n, lang) in documents]
# divide in two egal sets for training and testing
set_length = floor((len(featuresets)/2))
training_set = featuresets[set_length:]
testing_set =  featuresets[:set_length]
# create classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

# ----------------------- TEST THE CLASSIFIER ----------------------- 
tp = 0 # True positive
fp = 0 # False positive
fn = 0 # False negative
tn = 0 # True negative

# Accumulate data for confusion matrix
def confusion_matrix(sys_res, gold_res):
    global tp
    global fp
    global fn
    global tn
    if sys_res == gold_res:
        if sys_res: tp +=1
        else: tn += 1
    else:
        if gold_res: fn += 1
        else: fp += 1

confusion_matrix(classifier.classify(english_features("Ceci est une phrase en Francais")), False)
confusion_matrix(classifier.classify(english_features("This is an English sentence")), True)

# Test all brown
for id in brown.fileids():
    confusion_matrix(classifier.classify(english_features(" ".join(brown.words(id)))), True)

# test all uhdr
for id in udhr2.fileids():
    confusion_matrix(classifier.classify(english_features(" ".join(udhr2.words(id)))), False)

print("Precision : ", (tp/(tp+fp)))
print("Recall : ", (tp/tp+fn))
print("Accuracy : ", ((tp+tn)/(tp+fp+tn+fn)))
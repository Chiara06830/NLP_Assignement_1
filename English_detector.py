from nltk.corpus.reader.util import *
from nltk.metrics import ConfusionMatrix
from math import floor
import random
import nltk.data
nltk.download('udhr2')
nltk.download('ppattach')
nltk.download('movie_reviews')

# ----------------------- TRAIN A CLASSIFIER ----------------------- 
# open corpus
short_en = open(nltk.data.find('corpora/udhr2/eng.txt')).read() # english
short_en2 = open(nltk.data.find('corpora/movie_reviews/pos/cv878_15694.txt')).read() # english
short_fr = open(nltk.data.find('corpora/udhr2/fra.txt')).read() # non-english
short_tyv = open(nltk.data.find('corpora/udhr2/tyv.txt')).read() # non-english

# prepare list of examples and corresponding labels
documents = []
for r in short_en.split('\n'):
    documents.append((r, "en"))
for r in short_en2.split('\n'):
    documents.append((r, "en"))
for r in short_fr.split('\n'):
    documents.append((r, "non_en"))
for r in short_tyv.split('\n'):
    documents.append((r, "non_en"))
random.shuffle(documents)

# decide what feature is relevant, here: the whole word
def english_features(word) :
    return {'word': word.lower().lstrip()}

# set of features based on corpus
featuresets = [(english_features(n), lang) for (n, lang) in documents]
# divide in two egal sets for training and testing
training_set = featuresets[:floor((len(featuresets)*0.8))]
testing_set =  featuresets[floor((len(featuresets)*0.8)):]
print ("Training on ", len(training_set), "sentences")
print ("Testing on ", len(testing_set), "sentences")
# create classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

# ----------------------- TEST THE CLASSIFIER -----------------------
# gold data based on training set
gold = [label[1]for label in training_set]
# test data based on testing set
test = [label[1]for label in testing_set]
# calcul of confusion matrix
cm = nltk.ConfusionMatrix(gold[:len(testing_set)], test)
print("\n-----------CONFUSION MATRIX----------\n")
print(cm)
print("\n--------------MEASURMENT-------------\n")
print(cm.evaluate())
# calcul of accuracy 
print("Accuracy: ", nltk.classify.accuracy(classifier, testing_set), "\n")

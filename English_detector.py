from nltk.corpus import *
from nltk.corpus.reader.util import *
from nltk.metrics import ConfusionMatrix
import nltk.data
nltk.download('udhr2')
nltk.download('ppattach')
nltk.download('movie_reviews')
import random
from math import floor

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
set_length = floor((len(featuresets)/2))
training_set = featuresets[set_length:]
testing_set =  featuresets[:set_length]
# create classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

# ----------------------- TEST THE CLASSIFIER -----------------------
# calcul of accuracy 
print("Accuracy: ", nltk.classify.accuracy(classifier, testing_set), "\n")

# gold data based on training set
gold_set = [[token[1] for token in gold_actu] for gold_actu in[nltk.pos_tag(nltk.word_tokenize(sentence[0])) for sentence in documents[set_length:]]]
gold = []; [[gold.append(token) for token in elem]for elem in gold_set]
# test data based on testing set
test_set = [[token[1] for token in test_actu]for test_actu in[nltk.pos_tag(nltk.word_tokenize(sentence[0])) for sentence in documents[:set_length]]]
test = []; [[test.append(token) for token in elem]for elem in test_set]
# calcul of confusion matrix
cm = nltk.ConfusionMatrix(gold[:3000], test[:3000])
print(cm.evaluate())

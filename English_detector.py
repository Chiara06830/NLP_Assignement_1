from nltk import *
from nltk.corpus import *
from nltk.tokenize import RegexpTokenizer
from gensim.models import Word2Vec

tp = 0 # True positive
fp = 0 # False positive
fn = 0 # False negative
tn = 0 # True negative

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

def english_words(input):
    # each words of sentence
    input_set = set([word.lower() for word in RegexpTokenizer(r'\w+').tokenize(input)])
    # each words of english
    en_set = set(words.words('en'))
    common_elem = input_set.intersection(en_set)
    return len(common_elem) >= len(input_set)*0.8
    # input_model = Word2Vec(sentences=RegexpTokenizer(r'\w+').tokenize(input), vector_size=100, window=5, min_count=1, workers=4)
    # model = Word2Vec(sentences=words.words('en'), vector_size=100, window=5, min_count=1, workers=4)

confusion_matrix(english_words(brown.raw()), True)
confusion_matrix(english_words("Hello, how are you ?"), True)
confusion_matrix(english_words("Bonjour, comment ca va ?"), False)

print("Precision : ", (tp/(tp+fp)))
print("Recall : ", (tp/tp+fn))
print("Accuracy : ", ((tp+tn)/(tp+fp+tn+fn)))

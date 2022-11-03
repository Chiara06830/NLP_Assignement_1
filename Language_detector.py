from nltk import *
from nltk.corpus import *

def lang_ratio(input):
    lang_ratio={}
    # each words of sentence
    words = [word.lower() for word in wordpunct_tokenize(input)]
    for language in stopwords.fileids(): # for each language
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        lang_ratio[language] = len(common_elements)
    return lang_ratio 

def detect_language(input):
    ratios = lang_ratio(input)
    lang = max(ratios, key = ratios.get)
    return lang

ans = 'Y'
while((ans=='y')|(ans=='Y')):
    input1 = input("Write a scentence\n")
    lang = detect_language(input1)
    print(input1+"\t Langauge: "+ lang)
    ans = input("Continue ? (y/n)")

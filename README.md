# Assignement 1
## Instruction
The assignment consists in the development, in NLTK a Naïve Bayes Classifier able to detect a single class in one of the corpora available as attachments to the chosen package, by distinguishing ENGLISH against NON-ENGLISH. In particular the classifier has to be:

1. Trained on a split subset of the chosen corpus, by either using an existing partition between sample documents for training and for test or by using a random splitter among the available ones;
2. Devised as a pipeline of any chosen format, with word2vec on a list of words obtained by one of the available lexical resources.

The test of the classifier shall give out the measures of **accuracy**, **precision**, **recall** on the obtained confusion matrix.

## Results
This programme is trained on four corpus. Two in english one in French and on in Tuva, unified in same array with tag `en` or `non-en`.  
Each sentences in this array is transformed in lower case and with no space at beginning and end of it.
This array is divided in two set: the training set (80%) and the testing set (20%).  
Then the classifier is trained on training set and accuracy precision and recall on testing set.

A possible output is:
```
Training on  531 sentences
Testing on  133 sentences

-----------CONFUSION MATRIX----------

       |     n |
       |     o |
       |     n |
       |     _ |
       |  e  e |
       |  n  n |
-------+-------+
    en |<10>34 |
non_en | 35<54>|
-------+-------+
(row = reference; col = test)


--------------MEASURMENT-------------

   Tag | Prec.  | Recall | F-measure
-------+--------+--------+-----------
    en | 0.2222 | 0.2273 | 0.2247
non_en | 0.6136 | 0.6067 | 0.6102

Accuracy:  0.631578947368421 
```

## Comments on the experience
**Size of the corpus:** Corpus must have enough words to cover a maximum of possibility. But it is useless to have too many words because it won't cover a lot more of possibility but it will slow down the program. In this case 500 senteces is enough to see major differences between english and non-english.  
**Size of split training and test sets:**  It need more sentences to train than to test because it need to cover more case in training to understand all of testing. 80% for training and 20% for testing is a classic way to do it.  
**Performance indicator:** Accuracy is 0.6, it means that in 60% of time this classifier work. Precision show that for english sentences 22% where relevant and 61% for non-english. And it's almost the same for Recall.  
Obviously this score isn't the best, to improve this classifier we may train and tests it on other corpus to eventualy found a better accuracy.
# Assignement 1
## Instruction
The assignment consists in the development, in NLTK a Naïve Bayes Classifier able to detect a single class in one of the corpora available as attachments to the chosen package, by distinguishing ENGLISH against NON-ENGLISH. In particular the classifier has to be:

1. Trained on a split subset of the chosen corpus, by either using an existing partition between sample documents for training and for test or by using a random splitter among the available ones;
2. Devised as a pipeline of any chosen format, with word2vec on a list of words obtained by one of the available lexical resources.

The test of the classifier shall give out the measures of **accuracy**, **precision**, **recall** on the obtained confusion matrix and WILL NOT BE EVALUATED ON THE LEVEL OF THE PERFORMANCES. In other terms, when the confusion is produced, then the value of the assignment will be good, independently of the percentage of false positive and negative results.

Deliver a short set of comments on the experience (do not deliver the entire code, but link it on a public repository like GitHub or the GATE Repo). Discuss: size of the corpus, size of the split training and test sets, performance indicators employed and their nature, employability of the classifier as a Probabilistic Language Model.

## Results
This programme is trained on four corpus. There is has much english as non-english, unified in same array with tag `en` or `non-en`.  
Each sentences in this array is transformed in lower case and with no space at beginning and end of it.
This array is divided in two set of equal size: the training set and the testing set.  
Then the classifier is trained on training set and accuracy precision and recall on testing set.

A possible output is:
```
Accuracy:  0.6265060240963856 

 Tag | Prec.  | Recall | F-measure
-----+--------+--------+-----------
   ( | 0.0000 | 0.0000 | 0.0000
   ) | 0.0000 | 0.0000 | 0.0000
   , | 0.0390 | 0.0397 | 0.0393
   . | 0.0294 | 0.0345 | 0.0317
   : | 0.0000 | 0.0000 | 0.0000
  CC | 0.0513 | 0.0412 | 0.0457
  CD | 0.0222 | 0.0182 | 0.0200
  DT | 0.0643 | 0.0600 | 0.0621
  FW | 0.0559 | 0.0556 | 0.0557
  IN | 0.0862 | 0.0806 | 0.0833
  JJ | 0.1092 | 0.1123 | 0.1107
 JJR | 0.0000 | 0.0000 | 0.0000
 JJS | 0.0000 | 0.0000 | 0.0000
  MD | 0.0476 | 0.0400 | 0.0435
  NN | 0.2342 | 0.2331 | 0.2337
 NNP | 0.2109 | 0.2317 | 0.2208
NNPS | 0.0000 | 0.0000 | 0.0000
 NNS | 0.0662 | 0.0581 | 0.0619
 PDT | 0.0000 | 0.0000 | 0.0000
 POS | 0.0000 | 0.0000 | 0.0000
 PRP | 0.0000 | 0.0000 | 0.0000
PRP$ | 0.0000 | 0.0000 | 0.0000
  RB | 0.0000 | 0.0000 | 0.0000
 RBR | 0.0000 | 0.0000 | 0.0000
 RBS | 0.0000 | 0.0000 | 0.0000
  RP | 0.0000 | 0.0000 | 0.0000
  TO | 0.0000 | 0.0000 | 0.0000
  VB | 0.0189 | 0.0189 | 0.0189
 VBD | 0.0000 | 0.0000 | 0.0000
 VBG | 0.0000 | 0.0000 | 0.0000
 VBN | 0.0476 | 0.0645 | 0.0548
 VBP | 0.0222 | 0.0189 | 0.0204
 VBZ | 0.0000 | 0.0000 | 0.0000
 WDT | 0.0000 | 0.0000 | 0.0000
  WP | 0.0000 | 0.0000 | 0.0000
 WP$ | 0.0000 | 0.0000 | 0.0000
 WRB | 0.0000 | 0.0000 | 0.0000
  `` | 0.0000 | 0.0000 | 0.0000
```
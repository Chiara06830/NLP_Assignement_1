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
Tag | Prec.  | Recall | F-measure
-----+--------+--------+-----------
   ( | 0.0000 | 0.0000 | 0.0000
   ) | 0.0000 | 0.0000 | 0.0000
   , | 0.0435 | 0.0630 | 0.0514
   . | 0.0337 | 0.0306 | 0.0321
   : | 0.0000 | 0.0000 | 0.0000
  CC | 0.0345 | 0.0353 | 0.0349
  CD | 0.0185 | 0.0213 | 0.0198
  DT | 0.0513 | 0.0584 | 0.0546
  FW | 0.0330 | 0.0395 | 0.0359
  IN | 0.0829 | 0.0838 | 0.0833
  JJ | 0.0898 | 0.0735 | 0.0808
 JJR | 0.0000 | 0.0000 | 0.0000
 JJS | 0.0000 | 0.0000 | 0.0000
  MD | 0.0000 | 0.0000 | 0.0000
  NN | 0.1921 | 0.1915 | 0.1918
 NNP | 0.1500 | 0.1372 | 0.1433
NNPS | 0.0000 | 0.0000 | 0.0000
 NNS | 0.0338 | 0.0347 | 0.0342
 PDT | 0.0000 | 0.0000 | 0.0000
 POS | 0.0000 | 0.0000 | 0.0000
 PRP | 0.0000 | 0.0000 | 0.0000
PRP$ | 0.0000 | 0.0000 | 0.0000
  RB | 0.0000 | 0.0000 | 0.0000
 RBR | 0.0000 | 0.0000 | 0.0000
 RBS | 0.0000 | 0.0000 | 0.0000
  RP | 0.0000 | 0.0000 | 0.0000
  TO | 0.0182 | 0.0250 | 0.0211
  VB | 0.0000 | 0.0000 | 0.0000
 VBD | 0.0000 | 0.0000 | 0.0000
 VBG | 0.0000 | 0.0000 | 0.0000
 VBN | 0.0000 | 0.0000 | 0.0000
 VBP | 0.0000 | 0.0000 | 0.0000
 VBZ | 0.0149 | 0.0143 | 0.0146
 WDT | 0.0000 | 0.0000 | 0.0000
  WP | 0.0000 | 0.0000 | 0.0000
 WP$ | 0.0000 | 0.0000 | 0.0000
 WRB | 0.0000 | 0.0000 | 0.0000
  `` | 0.1667 | 0.1250 | 0.1429

Accuracy:  0.6144578313253012
```
import numpy as np
a = np.load(r'/root/autodl-tmp/CLUENER2020/BERT-LSTM-CRF/data/clue/test.npz', allow_pickle=True)
index = 0
words = a['words']
labels = a['labels']
print(words[0])
print(labels[0])


from bert_embedding import *

text = 'After stealing money from the bank vault, the bank robber was seen fishing on the Mississippi river bank.'

bert = bert_evaluation()

d = bert.embed(text)
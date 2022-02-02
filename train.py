from transformers import BertTokenizer
import pandas as pd
print('Loading BERT tokenizer...')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

X = []
max_len = 0

b = pd.read_csv("b.csv") .iloc[:, 2]
e = pd.read_csv("e.csv").iloc[:, 2]
m = pd.read_csv("m.csv").iloc[:, 2]
t = pd.read_csv("t.csv").iloc[:, 2]

b = [tokenizer.encode(sent, add_special_tokens=True) for sent in b]
e = [tokenizer.encode(sent, add_special_tokens=True) for sent in e]

m = [tokenizer.encode(sent, add_special_tokens=True) for sent in m]

t = [tokenizer.encode(sent, add_special_tokens=True) for sent in t]

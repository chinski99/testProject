# take sample text and tokenize it using Punkt

from nltk.tokenize import sent_tokenize
import os
import fnmatch

orig="/users/apple/Documents/tlumaczenia/tekst1/orig.txt"
path="/users/apple/Documents/tlumaczenia/tekst1"

with open(orig,"rt") as f:
    texto=f.read()
sto = sent_tokenize(texto)
tlum=[]

for file in os.listdir(path):
    if fnmatch.fnmatch(file, 'tlum*.txt'):
        with open(path+"/"+file,"rt") as f:
            text=f.read()
            st = sent_tokenize(text)
            tlum.append(st)

comp=zip(sto,*tlum)

for x in comp:
    for i,s in enumerate(x):
        print(i," ",s)
    print("-"*20)



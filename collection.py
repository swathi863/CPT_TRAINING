from collections import Counter
text=input("enter a text:")
counter=Counter(text)
#print("Characters frequencies:",dict(counter))
# counting of words
res=text.split()
k=Counter(res)
print(k)
max_word=max(k,key=k.get)
print(max_word)


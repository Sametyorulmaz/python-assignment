word = "hippo runs to us!"
dictt = {}
for i in word :
  dictt[i] = dictt.get(i, 0) + 1
print(dictt)
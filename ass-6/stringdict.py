text = "Python is fun and Python is powerful"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
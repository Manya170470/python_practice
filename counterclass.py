from collections import Counter

arr = [1,2,3,4,5,1,2,2,3,1,3]
freq = Counter(arr)
print(freq)
print(freq[1])
print(freq.most_common())
print(freq.most_common(2))
print(list(freq.elements()))
freq.update([1,1,1])
print(freq)

s = "bananas"
count = Counter(s)
print(count)
print(count["m"])

sentence = "This is the practice program for Counter class in Python . Python is a very cool language."
words = sentence.split()
print(Counter(words))

#first non repeating character in a string
str ="aabbcdde"
c = Counter(str)
for x in str:
    if c[x] == 1:
        print(x)
        break
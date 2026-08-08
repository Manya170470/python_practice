from collections import defaultdict

freq = defaultdict(int)
arr = [1,1,1,1,2,3,3,3,3,3,4,4]
for x in arr:
    freq[x] += 1
print(freq)
print(max(freq, key = freq.get)) #gives element which has the highest frequency
print(min(freq))                 #give the highest or lowest frequency

d = defaultdict(list)
d['a'].append(11)
d['b'].append(12)
print(d)

s = defaultdict(set)
s['python'].add("easy")  #as its set, no duplicate will be added
s['python'].add("easy")
print(s)

#check for duplicates in an array
array = [1,2,3,1,3,4,5,6]
seen = set()
for num in array:
    if num in seen:
        print("{} has duplicate".format(num))
    seen.add(num)

#intersection of two array
a = [1,2,3]
b = [2,4,5]
print(set(a) & set(b))




# Number hashing
n = int(input())
arr = list(map(int, input().split()))
hash_arr = [0] * 13  # Since values are assumed to be in the range 0 to 12
for num in arr:
    hash_arr[num] += 1
# Queries: the number we want to know frequency of
q = int(input())
while q > 0:
    number = int(input())
    print(hash_arr[number])
    q -= 1 

#character hashing through arrays
s = input("Enter the string")
hash_arr2 = [0] * 26 
for ch in s:
    hash_arr2[ord(ch) - ord('a')] += 1
p = int(input("Enter no of queries"))
for _ in range(p):
    letter = input()
    print(hash_arr2[ord(letter) - ord('a')])

#all 256 ASCII characters
str = input("Enter the string")
hash_arr3 = [0] * 256
for ch in str:
    hash_arr3[ord(ch)] += 1
r = int(input("Enter no of queries"))
for i in range(r):
    tocheck = input("Enter the {} query".format(i + 1))
    print(hash_arr3[ord(tocheck)])
    
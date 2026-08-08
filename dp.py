#M colouring
def IsPossibleToColour(node, col):
    for neighbour in graph[node]:
        if colour[neighbour] == col:
            return False
    return True
def Mcolouring(node):
    if node == n:
        return True
    for col in range(1, m+1):
        if IsPossibleToColour(node, col):
            colour[node] = col
            if Mcolouring(node + 1):
                return True
            colour[node] = 0
    return False

graph = [
    [1, 2],      
    [0, 2, 3],   
    [0, 1, 3],   
    [1, 2]       
]
n = len(graph)
m = 3                  
colour = [0] * n      
if Mcolouring(0):
    print(colour)
else:
    print("No solution exists")


#Palindrome partitioning
def solve(s, ind, path, ans):
    if ind == len(s):
        ans.append(path[:])
        return
    for i in range(ind, len(s)):
        if Palindrome(s, ind, i):
            path.append(s[ind:i + 1])
            solve(s, i + 1, path, ans)
            path.pop()

def Palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "aabb"
ans = []
solve(s, 0, [], ans)
print(ans)

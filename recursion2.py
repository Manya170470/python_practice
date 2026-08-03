def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))         
# TC: O(n), SC: O(n)

def fibonnaci(n):
    if n == 1 or n == 0:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)
print(fibonnaci(5))
#TC: O(2^n)

def summation(n):
    if n == 0:
        return 0
    return n + summation(n-1)

print(summation(4))

def reverseArray1(arr, l, r): #two pointer
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverseArray1(arr, l + 1, r - 1)
arr = [9,8,7,6,5,4,3,2,1]
reverseArray1(arr, 0, len(arr)-1)
print(arr)

def reverseArray2(i):  #one pointer
    n = len(arr)
    if i >= n//2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return reverseArray2(i+1)
print(reverseArray2(0))

def StrPalindrome(i, str):
    n = len(str)
    str = str.lower()
    if i >= n //2:
        return True 
    if str[i] != str[n-i-1]:
        return False 
    return StrPalindrome(i+1, str)
print(StrPalindrome(0, "Madam"))


    
    

    
    






    






def PrintSubsequence(arr, current, ind):
    if ind == len(arr):
        print(current)
        return 
    current.append(arr[ind])
    PrintSubsequence(arr, current, ind+1)
    current.pop()
    PrintSubsequence(arr, current, ind+1)
PrintSubsequence([3,2,1], [], 0)


def SubsequenceWithSumK(arr, current_sum, ds, ind, k):
    if ind == len(arr):
        if current_sum == k:
            print(ds)
        return
    ds.append(arr[ind])
    current_sum += arr[ind]
    SubsequenceWithSumK(arr, current_sum, ds, ind+1, k)
    ds.pop()
    current_sum -= arr[ind]
    SubsequenceWithSumK(arr, current_sum, ds, ind+1, k)
SubsequenceWithSumK([1,2,1],0,[], 0, 2)


def OnlyoneSubsequenceWithSumK(arr, current_sum, ds, ind, k):
    if ind == len(arr):
        if current_sum == k:
            print(ds)
            return True
        return False 
    current_sum += arr[ind]
    ds.append(arr[ind])
    if OnlyoneSubsequenceWithSumK(arr, current_sum, ds, ind+1, k):
        return True
    current_sum -= arr[ind]
    ds.pop()
    if OnlyoneSubsequenceWithSumK(arr,current_sum, ds, ind+1, k):
        return True 
    return False
        
OnlyoneSubsequenceWithSumK([1,2,1], 0, [], 0, 2)


def CountSubsequenceWithSumK(arr, current_sum, ind, k):
    if ind == len(arr):
        if current_sum == k:
            return 1 
        return 0 
    left = CountSubsequenceWithSumK(arr, current_sum + arr[ind], ind +1, k)
    right = CountSubsequenceWithSumK(arr, current_sum, ind +1, k)

    return left + right 

arr = [1,2,1]
k = 2 
print(CountSubsequenceWithSumK(arr, 0 , 0, k))

def PrintPermutations1(arr, ds, visited, ans):
    if len(ds) == len(arr):
        ans.append(ds.copy())
        return 
    for i in range(len(arr)):
        if i not in visited:
            ds.append(arr[i])
            visited[i] = True 
            PrintPermutations1(arr, ds, visited, ans)
            ds.pop()
            del visited[i]
arr = [1,2,3]
ans = []
PrintPermutations1(arr, [], {}, ans)
print(ans)

def PrintPermutations2(arr, ind, ds):
    if ind == len(arr):
        ds.append(arr.copy())
        return 
    for i in range(ind, len(arr)):
        arr[i], arr[ind] = arr[ind], arr[i]
        PrintPermutations2(arr, ind +1, ds)
        arr[i], arr[ind] = arr[ind], arr[i]
arr = [1,2,3]
ans = []
PrintPermutations2(arr, 0, ans)
print(ans)
        

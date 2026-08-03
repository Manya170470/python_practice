def CombinationSum1(arr, ind, target, ds):
    if ind == len(arr):
        if target == 0:
            print(ds)
        return 
    if arr[ind] <= target:
        ds.append(arr[ind])
        CombinationSum1(arr, ind, target - arr[ind], ds)
        ds.pop()
    CombinationSum1(arr, ind + 1, target, ds)
CombinationSum1([2,3,6,7], 0, 7, []) 


def CombinationSum2(arr, target):
    arr.sort()
    ans = []
    def backtrack(start, target, path):
        if target == 0:
            ans.append(path[:])
            return 
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            if arr[i] > target:
                break
            path.append(arr[i])
            backtrack(i+1, target - arr[i], path)
            path.pop()
    backtrack(0, target, [])
    return ans
print(CombinationSum2([1,1,1,2,2], 4))


def SubSetSum1(arr, ind, sum, ans):
    if ind == len(arr):
        ans.append(sum)
        return 
    SubSetSum1(arr, ind + 1, sum + arr[ind], ans)
    SubSetSum1(arr, ind + 1, sum, ans)
arr = [3, 1, 2]
ans = []
SubSetSum1(arr, 0, 0, ans)
ans.sort(reverse=True)
print(ans)

def Subset2(arr):
    arr.sort()
    ans = []
    def backtrack(start, path):
        ans.append(path[:])
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i - 1]:
                continue
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return ans
print(Subset2([1,2,2]))




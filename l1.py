def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    return -1
arr = [101, 102, 103, 104, 105] 
target = 104
result=linear_search(arr,target)
if(result!=-1):
    print("element found at index {result}")
else:
    print("Element not found")
  
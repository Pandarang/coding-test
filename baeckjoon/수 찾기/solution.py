import sys

def binary_search(arr, target) :
    left = 0
    right = len(arr) - 1
    
    while left <= right :
        mid = (left + right) // 2
        
        if arr[mid] == target :
            return True
        elif arr[mid] < target :
            left = mid + 1
        else :
            right = mid - 1
    
    return -1


n = int(input()) 
arrN = list(map(int, input().split()))
arrN.sort()

m = int(input()) 
arrM = list(map(int, input().split()))

for i in arrM :
    if binary_search(arrN, i) == True :
        print(1)
    else :
        print(0)


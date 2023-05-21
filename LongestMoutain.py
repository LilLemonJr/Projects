# Longest Moutain Subarray

# Time Complexity: O(n)
# Auxiliary Space: O(1)

# equivalent python code
import math
 
def LongestMountain(arr):
    n = len(arr)

# 1. First of all, we check the size of the vector or array. 
# 2. If the size of the array is less than 3, it means we do not have any type of mountain, hence return 0. 
    if n < 3: 
        return 0
    
    ans = 0
    i = 1

# 3. After this traverse the array and try to find the peak element by using the following condition:
# 4. If it is true then proceed the step 5 else increment the traversing pointer.
    while i <= n - 2:
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count = 0

            # now we find the index where a peak is present
            # 5. Now we are at the peak element of the array, so we take a count integer(to count the length of the subarray) and a pointer ‘j‘, it go the left side of the array to find the left side of the subarray and ‘i’ goes to the right side to find the right part of the subarray
            
            j = i # making a temporary element to help us traverse the array using two pointer techniques
            while j > 0 and arr[j] > arr[j - 1]:
                count += 1
                j -= 1
            while i <= n - 2 and arr[i] > arr[i + 1]:
                count += 1
                i += 1
            ans = max(ans, count)
        else:
            i += 1
    if ans > 0:
        return ans + 1
    return ans
 
# Driver code
d = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
print(LongestMountain(d))
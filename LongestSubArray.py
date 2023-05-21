# Longest sub-array having sum S

# Time Complexity: O(N), where N is the length of the given array.
# Auxiliary Space: O(N), for storing the maxLength in the HashMap.

def lenOfLongSubarr(A, n, S):
 
    # dictionary mydict implemented as hash map
    mydict = dict()
 
    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0

    # traverse the given array
    for i in range(n):
 
        # accumulate the sum
        sum += A[i]
 
        # when subArray starts from index '0'
        if (sum == S):
            maxLen = i + 1
 
        # check if 'sum-S' is present in
        # mydict or not
        elif (sum - S) in mydict:
            maxLen = max(maxLen, i - mydict[sum - S])
 
        # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i
 
    return maxLen
 
# Driver Code
if __name__ == '__main__':
    
    A = [0, 1, 0, 1, 1, -1, 1]
    n = len(A)
    S = 2

    print("Length =", lenOfLongSubarr(A, n, S))
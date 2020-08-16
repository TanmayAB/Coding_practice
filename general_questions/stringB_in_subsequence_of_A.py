
# Given two strings A, B, count the number of unique ways in string A, to form a subsequence that is identical to the string B.

A = 'abcbcadsf'
B = 'abc'

# A = 'aaaaaaaaaaaaaa'
# B = 'aaa'

result = {"count": 0}

# Brute Force

def getSubSequences(A, B , indexA, indexB, builtString, result):
    if len(builtString) == len(B):
        result['count'] += 1
    if indexA > len(A) - 1 or indexB > len(B) - 1:
        return None
    if A[indexA] == B[indexB]:
        getSubSequences(A, B , indexA + 1, indexB + 1, builtString + A[indexA], result)
        getSubSequences(A, B , indexA + 1, indexB, builtString, result)
    else:
        getSubSequences(A, B , indexA+1, indexB, builtString, result)

getSubSequences(A, B , 0, 0, "", result)

print(result['count'])
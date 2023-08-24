# Two to One
# DESCRIPTION:
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    # My old solution was O(NlogN) time complexity
#     s = []
#     for c in a1:
#         if c in s:
#             continue
#         else:
#             s.append(c)
#     for c in a2:
#         if c in s:
#             continue
#         else:
#             s.append(c)
#     s.sort()
#     r = ""
#     for i in range(0,len(s)):
#         r += s[i]
#     return r

# This is my new solution, which is O(N) time complexity, where N is the length of the longest list
# This solution is more efficient due to the dictionary being alphabetically sorted
# Also is more efficient due to the O(1) operations for the dictionary itself
    long = []
    len1, len2 = len(a1), len(a2)
    length = max(len1,len2)
    alpha_used = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    
    for i in range(length):
        if i < len1:
            if alpha_used[a1[i]] == 0:
                alpha_used[a1[i]] = 1
        if i < len2:
            if alpha_used[a2[i]] == 0:
                alpha_used[a2[i]] = 1
    for key in alpha_used:
        if alpha_used[key] == 1:
            long.append(key)
    return ''.join(long)

# Grasshopper - Summation
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(num):
# this old solution is O(N) time complexity
    # sum = 0
    # for i in range(1,num+1):
    #     sum += i
    # return sum

# this new solution is O(1) time complexity and is more efficient because it is only one operation that
# needs to be performed and returned in constant time
    return (num+1)*num/2


def topKFrequent(nums, k):
    count = {}
    arr = [[] for i in range(len(nums)+1)]
    output = []
    for num in nums:
        count[num] = 1 + count.get(num,0)
    for key,v in count.items():
        arr[v].append(key)
    for i in range(len(arr) -1, 0, -1):
        for n in arr[i]:
            output.append(n)
            print(len(output))
            if len(output) == k:
                return output
print(topKFrequent([1,1,1,2,2,3],2))
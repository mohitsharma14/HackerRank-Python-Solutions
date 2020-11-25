"""
Approach 1 - This is based on iterating over each element

"""

def birthday(s, d, m):
    result = 0
    for i in range(len(s)):
        j = 0
        sumTotal = 0
        while(j < len(m)):
            sumTotal += s[i + j]
            j += 1
        if(sumTotal == d):
            result += 1
        if( i + j == len(s)):
            break
    return result



from itertools import combinations

"""
Approach 2 - Disclaimer - This code considers all possible combinations and not just 
the Consequtive one'. This also means that process time will increase with increase in
list length.

"""
def birthday(s, d, m):
	barLen = len(s)
	if m <= barLen:
		comb = list(combinations(s, m))
		count = 0
		for t in comb:
		    totalSum = 0
		    for i in range(0, len(t)):
		        totalSum = totalSum + t[i]        
		    if totalSum == d:        
		        count += 1
		return count
	else:
		print("Bar length is small then birth month.")





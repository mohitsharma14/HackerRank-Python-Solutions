""""
Given a list of elements get the all possibles sum of elements by droppig one element at a time. Save
all posisble outputs in list and return min and maximum values.

Example : Let's say list provided is 2, 4, 6, 8, 10

1. Sum 4 + 6 + 8 + 10 = 28
2. Sum 2 + 6 + 8 + 10 = 26
3. Sum 2 + 4 +  8 + 10 = 24
4. Sum 2 + 4 + 6 + 10 = 22
5. Sum 2 + 4 + 6 + 8 = 20

Final output will be to return the minimum and maximum values of the above results. 
And that would be - 20 28
"""

def main():
	arr = [2, 4, 6, 8, 10]
	print(dropOneMinMaxSum(arr))


def dropOneMinMaxSum(arr):
    sumValues = []
    for i in range(0, len(arr)): 
        
        if len(set(arr)) != 1:
            b = filter(lambda x: x != arr[i], arr)
            sumValues.append(sum(list(b)))
            
        if len(set(arr)) == 1:
            sumValues.append(sum(arr) - arr[i])     
            
        
    return int(min(sumValues)), int(max(sumValues))

if __name__ == "__main__":
	main()


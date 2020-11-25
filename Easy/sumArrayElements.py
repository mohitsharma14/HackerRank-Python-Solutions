"""
Given an array of integers, find the sum of its elements.
For example, if the array is [2,3,4] so return 9.
"""

# Adding numbers of an array
def main():
	print(simpleArraySum(ar = [1,2,3,4,5]))

def simpleArraySum(ar):
	sum = 0
	for i in range(0, len(ar)):
		sum = sum + ar[i]
	return(sum)

if __name__ == '__main__':
	main()

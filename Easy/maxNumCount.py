"""
Write a function to provide the count of maximum number in a given list.

For example, if list is 14, 14, 86, 86, 86
we know maximum number is 86 and thus output should be cout of 86 IE 3

output - 3
"""

def main():
	numlist = [14, 14, 86, 86, 86]
	print(maxNumCount(numlist))

def maxNumCount(numlist):
    maxNum = max(numlist)
    count = len(list(filter(lambda x : x == maxNum, numlist)))
    return count


if __name__ == "__main__":
	main()

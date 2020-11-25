"""
Write a function that provides the ratio of count of positve, negative and zero numbers in an array 
with total number of elements in an array.

For example :
[1,2,3, 0,0, -1, -1]

Output:
1. Ratio of positive numbers = 3/7 0.42857142
2. Ratio of negative numbers = 2/7 = 0.2857142
3. Ration of zero numbers = 2/7 = 0.2857142

"""
def main():
	arr = [1,1,-1,-1,-1, 0, 0]
	print(countLengthRatio(arr))

def countLengthRatio(arr):
    zero_count = 0
    pos_count = 0
    neg_count = 0
    
    array_length = len(arr)
    
    for i in range(0,array_length):
        if arr[i] == 0:
            zero_count += 1
        elif arr[i] > 0:
            pos_count += 1
        else:
            neg_count += 1
    return zero_count/array_length, pos_count/array_length, neg_count/array_length

 if __name__ == "__main__":
 	main()
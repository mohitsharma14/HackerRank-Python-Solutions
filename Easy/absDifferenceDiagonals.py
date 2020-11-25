"""
Write a function to provide the absolute difference between the sum 
of primary and secondary diagonal elements of 2D array.

For example :

[[1, 2, 4], 
[7, 6, 3], 
[8, 5, 9]]

primary diagonal sum = 1 + 6 + 9 = 16
secondary diaginal sum = 4 + 6 + 8 = 18

function should return 
final output = | 16 - 18| = 2
"""

def main():
    arr = [[12,12,24, 1], 
            [34,10, 9, 2], 
            [10, 20, 30, 4],
            [12, 35, 98, 2]]
    print(diagonalDifference(arr))

def diagonalDifference(arr):
    # Write your code here
    primary_daigonal_sum = 0
    secondary_daigonal_sum = 0
    
    rows = len(arr)
    cols = len(arr[0])

    for i in range(0, rows):
        for j in range(0, cols):
            if i == j:
                primary_daigonal_sum = primary_daigonal_sum + arr[i][j]
                
            if (i + j) == (rows - 1):
                secondary_daigonal_sum = secondary_daigonal_sum + arr[i][j]
                
    return abs(primary_daigonal_sum - secondary_daigonal_sum)

if __name__ == "__maine__":
    main()
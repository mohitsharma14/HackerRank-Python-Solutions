def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0, n): 
        for j in range(1, n):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count
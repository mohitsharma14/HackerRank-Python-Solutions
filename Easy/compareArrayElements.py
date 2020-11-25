"""
Given two arrays compare individual elements of each array. 
These arrays contain marks obtained by Ronit and Raj in 3 subjects.
award 1 point by comparing the each element of element. 
For example -

Ronit = (98, 83, 47)
Raj = (99, 78, 45)

Now Compare, 
1. a[0] with b[0], if a[0] > b[0] then Ronit gets 1 point
2. a[1] with b[1], if a[1] < b[1] then Raj gets 1 point
3. a[2] with b[2], if a[2] == b[2] then no one gets any point
"""

def main():
    a = [12, 25, 98]
    b = [45, 10, 89]
    print(compareResults(a, b))

# Complete the compareTriplets function below.
def compareResults(a, b):
    a_score = 0
    b_score = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            a_score = a_score + 1
        elif a[i] < b[i]:
            b_score = b_score + 1
        else:
            continue
    return a_score, b_score

if __name__ == "__main__":
    main()
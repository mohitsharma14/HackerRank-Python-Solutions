"""
Finding how many apples or oranges fell with in a particular range
Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

For example, Sam's house is between  and . The apple tree is located at  and 
the orange at . There are  apples and  oranges. Apples are thrown  units distance 
from , and  units distance. Adding each apple distance to the position of the tree, 
they land at . Oranges land at . One apple and two oranges land in the inclusive range  
so we print

Output
1
2

"""



# Approach 1 
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesDistCount = []
    orangesDistCount = []
    
    for i in range(0, len(apples)):
        tempVal = a + apples[i]
        if(tempVal in range(s, t+1)):
            applesDistCount += 1
    
    for i in range(0, len(oranges)):
        tempVal = a + oranges[i]
        if(tempVal in range(s, t+1)):            
            orangesDistCount += 1
    
    
        
    print(len(applesDistCount))
    print(len(orangesDistCount))
    
s = 7
t = 10

a = 4
b = 12

apples = [10, 3, -4]
oranges = [ 3, -7]
        
countApplesAndOranges(s, t, a, b, apples, oranges)       


# Approach - 2

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesDist = []
    orangesDist = []
    
    for i in range(0, len(apples)):
        applesDist.append(a + apples[i])
    
    for i in range(0, len(oranges)):
        orangesDist.append(b + oranges[i])
        
        finalDistApples = list(filter(lambda x: (x >= 7) and (x <= 10), applesDist))
        finalDistOranges = list(filter(lambda x: (x <= -7) and (x >=- 10), orangesDist))
    
        
    print(len(finalDistApples))
    print(len(finalDistOranges))

countApplesAndOranges(s, t, a, b, apples, oranges)
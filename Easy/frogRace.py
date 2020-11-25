"""
Write a function to firgure out if two frogs starting at different positions and with different speed
be at the same location at the same time during the race.

If yes, return YES
else, return NO.

The function takes 4 inputs -

x1 - position of frog 1 
v1 - jump speed of frog 1

x2 - position of frog 2 
v2 - jump speed of frog 2

"""

# Approach 1
def frogRace(x1, v1, x2, v2):
    if (x2 > x1) and (v2 > v1):
        return "NO"
    else:
        while x1 != x2:
            x1 += v1
            x2 += v2
            if x1 == x2:
                return "YES"

# Approach 2
def frogRace(x1, v1, x2, v2):
    if v1 > v2:
        if (x2 - x1) % (v2 - v1) == 0:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"



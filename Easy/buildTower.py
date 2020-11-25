"""
Write a function to create a tower of # like the one below. The height of tower is to be proved by the user.

let's say user provides height = 4, then output should be :

   #
  ##
 ###
####

"""

def main():
    height = int(input("Enter tower height: "))
    buildTower( height )

def buildTower(height):
    blanks = height-1

    for i in range(0, height):
        print( ' ' * blanks + "#" * i )
        blanks = blanks - 1

if __name__ == "__main__":
	main()

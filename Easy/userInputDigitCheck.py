"""
Write a function to check if the input provided by user
is a digit or not. If not, do not accept and abort.

Second Verison - Insead of aborting ask the user to enter again.

"""

def main():
	user_input = userInput()

# Option 1 - Where we abort
	if isDigit(user_input):
		n = int(user_input)
		print(f"Entered Number is {n}")
	else:
		print("Aborting!")

# Option 2 - Where we keep asking the user for input

	# while isDigit(user_input) == False:
	# 	user_input = userInput()

	# n = int(user_input)
	# print(f"Entered Number is {n}")


def isDigit(s):

    for i in range(len(s)):
    	if s[i].isdigit() != True:
            return False
    return True

def userInput():
	num = input("Enter a number: ")
	return num


if __name__ == "__main__":
	main()


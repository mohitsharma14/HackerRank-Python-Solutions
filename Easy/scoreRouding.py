"""
Write a function which rounds the marks of the student using the following rule.
1. If the difference between the grade and the next multiple of 5 is less than 3, round the marks 
	to next multiple. Example -  score is 68, next multiple of 5 is 70. Now, |67-70| < 3. Round the 
	grade to 70.

2. If score is less than 38 no change in marks as even after arounding the student still fails. Any 
	scores less than 40 even after rounding is a failing grade.

Input - [67, 22, 98, 51]
Output - [67, 22, 100, 51]

"""

def main():
	student_marks = [38, 98, 57, 62, 90, 27]
	scoreRouding(student_marks)

def scoreRouding(marks):

	final_scores = []

	for mark in marks:
		if mark >= 35:
		    getNextFiveMultiple = nextFiveMultiple(mark)
		    if mark != getNextFiveMultiple and abs(mark - getNextFiveMultiple) < 3:
		        final_scores.append(getNextFiveMultiple)
		    else:
		         final_scores.append(mark)
		else:
		     final_scores.append(mark)
     return final_scores


def nextFiveMultiple(mark):
    if mark % 5 != 0:
        nextNum = ((mark // 5) + 1) * 5
        return nextNum
    else:
        return mark

if __name__ == "__marks__":
	main()
    
        



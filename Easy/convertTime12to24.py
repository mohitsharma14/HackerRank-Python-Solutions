
"""
Write a function to convert 12 hour clock to 24-hour time.

For Example: 12:00:00 AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
 and 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

def main():
    convertTime12to24("01:01:12 PM")
    
def convertTime12to24(string):
    if string[-2:] == "AM" and string[:2] == "12" :
        return "00" + string[2:-2]
    
    elif string[-2:] == "AM" :
        return string[:-2]
    
    elif string[-2:] == "PM" and string[:2] == "12" :
        return string[: -2]
    
    else:
        return str(int(string[:2]) + 12) + string[2:8]
    
if __name__ == "__main__":
    main()
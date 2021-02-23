import calendar

# This is the doomsday algorithm which can take in any current era date and relay what day of the week it occured
inputYear = int(input("please input a year"))
leapYear = False
if inputYear % 4 == 0 and inputYear % 100 != 0:
    leapYear
elif inputYear % 400 == 0:
    leapYear

inputMonth = int(input("Please input a month as a number"))
inputDay = int(input("Please input a day as a number"))

daysInMonths =	{1: 31, 2: 29 if leapYear else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if(inputMonth > 12 or inputDay > daysInMonths.get(inputMonth)):
    raise IndexError("your chosen date does not exist")

# 400 year calender cycle
DoomsdayYears = [2, 0, 5, 3]
anchor = DoomsdayYears[(inputYear % 400) // 100]
simplifiedYears = inputYear % 100
total = (simplifiedYears // 12) + (simplifiedYears % 12) + ((simplifiedYears % 12) // 4)
Doomsday = (total + anchor) % 7

# these are the dates in each month which the doomsday will always match
months = [3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
if leapYear:
    months[0] = 4
    months[1] = 29

answer = ((inputDay - months[inputMonth - 1]) + Doomsday) % 7

print("the answer is", calendar.day_name[answer-1])
print("Doomsday =", Doomsday)
print("for,", inputMonth, "/", inputDay, "/", inputYear)
'''Jack is always excited about sunday. It is his favourite day, 
when he gets to play all day. And goes to cycling with his friends. 

So every time when the months starts he counts the number of sundays 
he will get to enjoy. Considering the month can start with any day, 
be it Sunday, Monday…. Or so on.

Count the number of Sunday jack will get within n number of days.

 Example 1:

Input 

mon-> input String denoting the start of the month.

13  -> input integer denoting the number of days from the start 
of the month.

Output :

2    -> number of days within 13 days.

Explanation:

The month start with mon(Monday). So the upcoming sunday 
will arrive in next 6 days. And then next Sunday in n
ext 7 days and so on.

Now total number of days are 13. It means 6 days to 
first sunday and then remaining 7 days will end up in another sunday. 
Total 2 sundays may fall within 13 days.'''

def count_sundays(start_day,total_days):
    w={'sun':0,'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6}
    start_idx=w[start_day.lower()]
    first_sunday=(7-start_idx)%7 # Findg days to 1st sunday
    if first_sunday==0:
        first_sunday=0 #Already a sunday
    rest_days=total_days-first_sunday
    if rest_days<0:
        return 0
    sundays=1+(rest_days//7)
    return sundays

start_day = input("Enter start day (mon, tue, ...): ").strip()
n_days = int(input("Enter number of days: "))
print(count_sundays(start_day, n_days))

def main():
    s = input()
    a = int(input())
    m = {
        "mon": 6, "tue": 5, "wed": 4,
        "thu": 3, "fri": 2, "sat": 1,
        "sun": 0
    }
#This dictionary gives days left to the next Sunday
#Example:
#"mon": 6 → if month starts on Monday, Sunday is 6 days away
#"sun": 0 → if month starts on Sunday, Sunday is today

    ans = 0
    if a - m[s[:3]] >= 1:
        ans = 1 + (a - m[s[:3]]) // 7
        #m[s[:3]] → get number of days to first Sunday (first 3 letters of day)
#a - m[s[:3]] → remaining days after the first Sunday
#1 + (remaining_days // 7) → first Sunday counts + additional Sundays every 7 days
    print(ans)

if __name__ == "__main__":
    main()
#Example Run

#Input:

#mon
#13

#Execution:

#Month starts on Monday → next Sunday in 6 days
#Remaining days = 13 - 6 = 7
#Sundays = 1 + 7 // 7 = 1 + 1 = 2

#Output:

#2



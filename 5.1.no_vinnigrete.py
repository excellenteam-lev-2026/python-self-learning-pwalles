import datetime
import random

def no_vinnaigrete(date1, date2):
    timeHelper=date2-date1
    seconds=timeHelper.total_seconds()
    seconds=int(seconds)
    random_seconds=random.randint(0,seconds)
    delta=datetime.timedelta(seconds=random_seconds)
    date3 = date1+delta
    return date3

if __name__ == "__main__":
    print("Enter the first date (YYYY-MM-DD):")
    date1_str = input()
    print("Enter the second date (YYYY-MM-DD) later from the first:")
    date2_str = input()
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    date3 = no_vinnaigrete(date1, date2)
    print("The date is:", date3.strftime("%Y-%m-%d"))
    if date3.isoweekday()==1:
        print("אין לי ויניגרט")

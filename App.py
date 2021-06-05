import calendar

try:
    y= int(input())
    if 1920>y or y>2100:
        print("please choose another year")
    else:
        for i in range (12):
            print(calendar.month(y,i+1))
except:
    print("please choose a year between 1920 and 2100")

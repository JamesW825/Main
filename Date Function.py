# This converts dates to a DD/MM/YYYY format

def date():
    #Months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    Wdate=input("Enter a date in a worded from. (Eg: 1st Jan 2022 - Including spaces)\n")
    Year=str(Wdate[-4:])
    Month=Wdate[4:],Wdate[-4:]
    Day=Wdate[4:]
    print("Date is: ", Day, Month, Year)

date()
fine=int(input("enter the fine"))
expectedday=int(input("enter the expected day"))
returnedday=int(input("enter the returnedday"))
days=expectedday-returnedday
days=returnedday-expectedday
if returnedday<expectedday:
    print("no fine")
else:
    print(fine*days)
expectedmonth=int(input("enter the expectedmonth"))
returnedmonth=int(input("enter the returnedmonth"))
month=expectedmonth-returnedmonth
month=returnedmonth-expectedmonth
if returnedmonth<expectedmonth:
    print("no fine")
else:
    print(fine*month)
expected_year=int(input("enter the expectdyear"))
returned_year=int(input("enter the returnedyear"))
year=expected_year-returned_year
year=returned_year-expected_year
if returned_year<expected_year:
    print("no fine")
else:
    print(fine*year)

time =float(input("enter the time"))
if time > 7.01:
    if time<=8.00:
        print("breakfast")
if time >=8.10:
    if time<=12.30:
        print("1st coding time") 
if time >=12.31:
    if time<= 14.00:
        print("lunch time") 
if time>=14.01:
    if time<=16.30:
        print("2nd coding")
if time>=16.35:
    if time==17.00:
        print("excrise")
if time>=17.01:
    if time<=18.00:
        print("break time") 
if time >=18.01:
    if time<=20.00:
        print("english class") 
if time>=20.01:
    if time<= 21.00:
        print("dinner time")
    else:
        print("sleeping")    

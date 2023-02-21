from datetime import date
import numpy as np
today = date.today()
def Year_Today():
    Year = today.year
    return Year
def Month_name_today():
    Month = today.month
    if Month==1:
        MN="January"
    elif Month==2:
        MN="February"
    elif Month==3:
        MN="March"
    elif Month==4:
        MN="April"
    elif Month==5:
        MN="May"
    elif Month==6:
        MN='June'
    elif Month==7:
        MN="July"
    elif Month==8:
        MN="August"
    elif Month==9:
        MN="Suptember"
    elif Month==10:
        MN="October"
    elif Month ==11:
        MN="November"
    elif Month==12:
        MN="December"
    
    else:
        print("I have a dought are you really from this planet")
    return MN

def CDate():
    t=print(today)
    return t

def Month_Name_oprational(Month):
    if Month==1:
        MN="January"
    elif Month==2:
        MN="February"
    elif Month==3:
        MN="March"
    elif Month==4:
        MN="April"
    elif Month==5:
        MN="May"
    elif Month==6:
        MN='June'
    elif Month==7:
        MN="July"
    elif Month==8:
        MN="August"
    elif Month==9:
        MN="Suptember"
    elif Month==10:
        MN="October"
    elif Month ==11:
        MN="November"
    elif Month==12:
        MN="December"
    else:
        print("I have a dought are you really from this planet")
    return MN

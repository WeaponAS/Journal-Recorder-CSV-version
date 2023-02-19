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

def Month_Name_Today_oprational(MNopration,MNScale):
    raise ConnectionAbortedError("This Module is still not finish building and have inpurities")
    MN=today.month
    ml=np.array[-1, -13, -25]
    while True:
        if MNopration=="+":
            newNM=MN-int(MNScale)
            break
        elif MNopration=="-":
            if MN-MNScale<1:
                temp=MN-MNScale
                if temp in ml:
                    newNM="December"
                elif temp in ml-1:
                    newNM="November"
                elif temp in ml-2:
                    newNM="October"
                elif temp in ml-3:
                    newNM="September"
                elif temp in ml-4:
                    newNM="August"
                elif temp in ml-5:
                    newNM="July"
                elif temp in ml-6:
                    newNM="June"
                elif temp in ml-7:
                    newNM="May"
                elif temp in ml-8:
                    newNM="April"
                elif temp in ml-9:
                    newNM="March"
                elif temp in ml-10:
                    newNM="February"
                elif temp in ml-11:
                    newNM="January"
                else:
                    print("Only Support for last 3 years")
            break
        else:
            print("Not a valid input")
    return newNM
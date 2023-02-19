import DayTimeMonth
import pandas as pd
import matplotlib.pyplot as plt

import os
from datetime import date

MN = DayTimeMonth.Month_name_today()
Year = DayTimeMonth.Year_Today()
file = "{}-{}.csv".format(MN, Year)
try:
    df = pd.read_csv(file)
except FileNotFoundError:
    df = pd.DataFrame([])
    df['Date'] = None
    df['Particular'] = None
    df['Note'] = None
    df['outflow'] = None
    df['inflow'] = None
    df.to_csv(file, index=False)
    print("CSV file Created")
except pd.errors.EmptyDataError:
    print("Empty DataFrame")
while True:
    print("\t\t\t\tMain Menu")
    print("_________________________________________________")
    # Changed inflow to income for clarity
    print("\nBalance : ", df.inflow.sum() - df.outflow.sum())
    print("1) Record Journal Entries")
    print("2) Show Statistics (by default this month) ")
    print("3) Analysis")
    print("0) Quit")
    MainOperation = int(input("\nEnter one of the above mentioned to perform Activity (Integer only): "))
    if MainOperation == 1:
        print("="*30)
        print("\n\nRecording Journal\n\n")
        Date = DayTimeMonth.CDate()
        particular = input("Particular : ")
        note = input("Note : ")
        outflow = int(input("Outflow Amount : "))
        income = int(input("Income Amount : "))
        new_index = df.index.max() + 1
        df.loc[new_index] = [Date, particular, note, outflow, income]
        print("Recorded")
        print(df.loc[new_index])
        df.loc[new_index] = [date.today(), particular, note, outflow, income]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Previous Entry is Recorded")
        df.to_csv(file,index=False)
    if MainOperation == 2:
        print("*"*30)
        print("Statistics")
        StatOption = input("Do you want to show stats of previous months (Y/N) : ")
        if StatOption.upper() == 'Y':
            Year = int(input("Enter year (YYYY): "))
            Month = int(input("Enter Month (MM): "))
            MN = DayTimeMonth.Month_name_today()
            try:
                statefile = "{}-{}".format(MN,Year)
            except FileNotFoundError:
                print("you may have deleted the file or \nthe file does not existed for file name {}".format(statefile))
            except pd.errors.EmptyDataError:
                print("this file is empty cannot perform ant action")
                break
            TempStat = pd.read_csv(statefile)
            print('Total : ',TempStat.inflow.sum()-TempStat.outflow.sum())
            SI = df['Particular'].unique()
            #Display Each Unique Record with Balance of Each Records
            for item in SI:
                tempdf = df[df['Particular']==item]
                total = tempdf['inflow'].sum() - tempdf['outflow'].sum()
                print(item + ":", total)
        elif StatOption.upper() == 'N':
            print('Current Total : ', df.inflow.sum() - df.outflow.sum())
            SI = df['Particular'].unique()
            for item in SI:
                tempdf = df[df['Particular'] == item]
                total = tempdf['inflow'].sum() - tempdf['outflow'].sum()
                print(item + ":", total)
    elif MainOperation==3:
        AnalysisOption=input("Do you Want to show This Month's Analysis (Y/N): ")
        if AnalysisOption.upper()=='Y':
            #display inflow and outflow for current month for each day
            df[["inflow","Outflow"]].plot(kind='bar',color=['Green','Red'])
            plt.show()            

    elif MainOperation == 3:
        AnalysisOption = input("Do you want to show this month's analysis (Y/N): ")
        if AnalysisOption.upper() == 'Y':
            # group the inflow and outflow by day and sum the values
            daily_summary = df.groupby(pd.Grouper(key="Date", freq="D"))["inflow", "outflow"].sum()
            # create a bar chart with the daily inflow and outflow values
            daily_summary.plot(kind='bar', color=['Green', 'Red'])
            plt.xlabel("Day of the Month")
            plt.ylabel("Amount")
            plt.title("Inflow and Outflow for Current Month")
            plt.show()
            plt.tight_layout()

        elif AnalysisOption.upper() == 'N':
        # group the inflow and outflow by day and sum the values
            Year = input("Enter Year (YYYY): ")
            Month = input("Enter Month (MM):")
            AnalysisFile = "{}-{}.csv".format(Year,Month)
            try:
                df=pd.read_csv(AnalysisFile)
            except FileNotFoundError:
                print("File do not exist")
            daily_summary = df.groupby(pd.Grouper(key="Date", freq="D"))["inflow", "outflow"].sum()
            # create a bar chart with the daily inflow and outflow values
            daily_summary.plot(kind='bar', color=['Green', 'Red'])
            plt.xlabel("Day of the Month")
            plt.ylabel("Amount")
            plt.title("Inflow and Outflow for Current Month")
            plt.show()
            plt.tight_layout()
    elif MainOperation==4:
        print("Created a CSV txt file")
        df.to_csv("read.txt",index=False)
        os.startfile(file)
    elif MainOperation == 0:
        print("Program created by Ayush Sharma")
        quit()
    else:
        print("'{}' Do not exist in this program please type integer for initial processing")
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

pd.options.display.float_format = '{:20,.2f}'.format
df1=pd.read_csv('countr1.csv',index_col=0)
df2=pd.read_csv('city1.csv',index_col=0)

def show():
  ch=int(input("ENTER 1 FOR COUNTRIES AND 2 FOR CITIES: "))
  if(ch==1):
    print(df1)
    b=int(input(" 1 FOR POPULATION_AFFECTED \n 2 FOR RECOVERED_CASES \n 3 FOR DEATH \n 4 FOR ACTIVE_CASES: "))
    if(b==1):
      print(df1['population_affected'])
    elif(b==2):
      print(df1['recovered_cases'])
    elif(b==3):
      print(df1['Death'])
    elif (b==4):
      print(df1['Active_cases'])
    else: 
      print("Invalid Choice")
  elif(ch==2):
    print(df2)
    b=int(input(" 1 FOR POPULATION_AFFECTED \n 2 FOR RECOVERED_CASES \n 3 FOR DEATH \n 4 FOR ACTIVE_CASES:  "))
    if(b==1):
      print(df2['population_affected'])
    elif(b==2):
      print(df2['recovered_cases'])
    elif(b==3):
      print(df2['Death'])
    elif (b==4):
      print(df2['Active_cases'])
    else: 
      print("Invalid choice, Try again")
  else: 
    print("Invalid Choice")

def stats():
 ch=int(input("ENTER 1 FOR COUNTRIES AND 2 FOR CITIES: "))
 if(ch==1):
    print(df1.describe())
    b=int(input(" 1 FOR POPULATION_AFFECTED \n 2 FOR RECOVERED_CASES \n 3 FOR DEATH \n 4 FOR ACTIVE_CASES : "))
    if(b==1):
      print(df1['population_affected'].describe())
    elif(b==2):
      print(df1['recovered_cases'].describe())
    elif(b==3):
      print(df1['Death'].describe())
    elif(b==4):
      print(df1['Active_cases'].describe())
    else:
      print("Invalid choice, Try again")
 elif(ch==2):
    print(df2.describe())
    b=int(input("ENTER 1 FOR POPULATION_AFFECTED \n 2 FOR RECOVERED_CASES \n 3 FOR DEATH \n 4 FOR ACTIVE_CASES: "))
    if(b==1):
      print(df2['population_affected'].describe())
    elif(b==2):
      print(df2['recovered_cases'].describe())
    elif(b==3):
      print(df2['Death'].describe())
    elif(b==4):
      print(df2['Active_cases'].describe())
    else: 
      print("Invalid choice, Try again")
 else: 
      print("Invalid choice, Try again")

def add():
  ch=int(input("ENTER 1 FOR COUNTRIES AND 2 FOR CITIES: "))
  if(ch==1):
    ch=int(input("ENTER 1 FOR rows AND 2 FOR columns: "))
    if(ch==1):
      r_name=input('Enter new row name:')
      r_value=int(input('Enter default row value:'))
      df1[r_name]=r_value
      print(df1)
    elif(ch==2):  
      col_name=input('Enter new column name:')
      col_value=int(input('Enter default column value: '))
      df1[col_name]=col_value
      print(df1)
    else: 
      print("Invalid choice, Try again")  
  elif(ch==2):
    ch=int(input("ENTER 1 FOR rows AND 2 FOR columns: "))
    if(ch==1):
      r_name=input('Enter new row name:')
      r_value=int(input('Enter default row value:'))
      df2[r_name]=r_value
      print(df2)
    elif(ch==2):  
      col_name=input('Enter new column name:')
      col_value=int(input('Enter default column value: '))
      df2[col_name]=col_value
      print(df2)
    else: 
      print("Invalid choice, Try again")
  else: 
      print("Invalid choice, Try again")      

def delr():
  ch=int(input("ENTER 1 FOR COUNTRIES AND 2 FOR CITIES: "))
  if(ch==1):
    ch=int(input("ENTER 1 FOR rows AND 2 FOR columns: "))
    if(ch==1):
      r=int(input('Enter the row number to be deleted" '))
      df=df1.drop(df1.index[r])
      print(df1)
    elif(ch==2):
      co=input('Enter the column name to be deleted: ')
      del df1[co]
      print(df1)
    else: 
      print("Invalid Choice") 
  elif(ch==2):
    ch=int(input("ENTER 1 FOR rows AND 2 FOR columns: "))
    if(ch==1):
      r=int(input('Enter the row number to be deleted: '))
      df=df2.drop(df2.index[r])
      print(df2)
    elif(ch==2):
      co=input('Enter the column name to be deleted: ')
      del df2[co]
      print(df2)
    else:
      print("Invalid Choice") 
  else: 
    print("Invalid Choice") 

def bargraph():
  ch=int(input("ENTER 1 FOR COUNTRIES BAR GRAPH AND 2 FOR CITIES BAR GRAPH:")) 
  if(ch==1):
    df1.plot.bar()
    pl.show() 
  elif(ch==2):
    df2.plot.barh()
    pl.show() 
  else: 
    print("Invalid choice, Try again") 

def test(): 
  a=input("Enter your response for a test :(Y/y/yes/YES)or(N/n/no/NO):") 
  if(a=="Y" or a=="y" or a=="Yes" or a=="yes" or a=="YES"):
    print("for yes, please type 'y', ""for no,please type 'n' ") 
    b=input("Are you having cold or dry cough? ") 
    d=input("Do you have headache or body-ache or chest pain ") 
    e=input("Do you feel weakness,tired,uneasiness or shortness of breath ")
    f=input("Do you have sore throat,conjunctivitis,rashes,itching? ") 
   
    if(b=='y' or d=='y' or e=='y' or f=='y'):
      print("You may have symptoms of coronavirus, get your self tested now.") 
    elif(b=='n' and d=='n' and e=='n' and f=='n'):
      print("You don't have coronavirus") 
    else: 
      print("Invalid choice, Try again")
  elif(a=="N" or a=="n" or a=="No" or a=="no" or a=="NO"):
     ch=input("To take Covid-19 self test press 1. To exit press 3. To go to menu again, press 5,") 
     if(ch==1): 
       test() 
     elif(ch==3):
        exit() 
     elif(ch==5):
        ans 
     else: 
       print("Invalid choice, Try again") 
  else: 
    print("Invalid choice, Try again")

ans=True
while ans: 
  print("\n\tUser specified menu\n") 
  print( " 1.Show World's Caseload\n",
   "2.Add date\n",
   "3.Delete data\n",
   "4.Statistical view\n", 
   "5.Graphical Representation\n", 
   "6.take a self corona test\n", 
   "7.Exit \n" )
 
  choice=int(input("Enter your numerical choice:"))
  if choice==1:
   show() 
  elif choice==2: 
    add() 
  elif choice==3:
    delr() 
  elif choice==4:
    stats() 
  elif choice==5:
    bargraph() 
  elif choice==6:
    test()
  elif choice==7:
    print("You have opted to come out of the menu", "THANK YOU. HOPE TO SERVE YOU NEXT TIME")
    exit()
  else: 
   print("Invalid Choice")

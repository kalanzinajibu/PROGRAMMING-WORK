#THIS WORK WAS DONE BY KALANZI NAJIBU 15/U/5556/PSA
#BSC. TELECOMMUNICATIONS ENGINEERING
import datetime
years =float(input('Enter your age:'))
month=int(input('Enter month of birth:'))
day=int(input('Date of birth:'))
days_per_year=365.24
birthdate =datetime.datetime.now()  - datetime.timedelta(days=(years*days_per_year))
y=int(birthdate.strftime("%Y"))
x=datetime.date(y,month,day)
print(x.strftime("You were born on %A, %d-%B-%Y"))

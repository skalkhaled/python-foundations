from datetime import datetime
def check_birthdate(year,month,day):
    today = datetime(2020,1,26)
    birthdate = datetime(year, month, day)
    if today > birthdate:
        return True 
    return False

def calculate_age(year,month,day):
    today = datetime(2020,1,26)
    birthdate = datetime(year, month, day)
    user_age = int((today - birthdate).days / 365)
    print("You are %s years old" % user_age)
   
year = input("Enter year of birth")
month = input("Enter month of birth")
day = input("Enter day of birth")
calculate_age(int(year),int(month),int(day))

if check_birthdate(int(year),int(month),int(day)) ==True:
    calculate_age(int(year),int(month),int(day))
else:
    print("Birthdate is invalid")


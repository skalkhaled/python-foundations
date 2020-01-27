skills = ["Eating", "Running", "Swimming", "Painting"]
cv = {}
cv["name"] = input("What is your name? ")
cv["age"] = int(input("What is your age? "))
cv["experience"] = int(input("How many years of experience? "))
cv["skills"] = []

counter = 0
for skill in skills:
    print("%d. %s" %(counter+1, skill))
    counter+=1

skill1 = input("Choose a skill from the list")

if skill1.isdigit:
    cv['skills'].append(skills[int(skill1)-1])
else:
    skill1 = input("Invalid number, try again")

skill2 = input("Choose a second skill from the list")

if skill2.isdigit:
    cv['skills'].append(skills[int(skill2)-1])
else:
    skill2 = input("Invalid number, try again")

print(cv)
if cv["age"] < 35 and cv['age']>18 and cv['experience']>3 and "Running" in cv['skills']:
    print("Accepted")
else:
    print("Not Accepted")


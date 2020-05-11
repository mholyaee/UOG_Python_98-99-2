person=dict()
while True:
    name=input("name:")
    if name=="finish":
        break
    age=input("age:")
    age=int(age)
    if name in person:# if there are several persons with the same name, we should save the age of the oldest man!
        if age>person[name]:
            person[name] = age
    else:
        person[name] = age

Maxage=0
for x,y in person.items():
    if y>Maxage:
        Maxage=y
        Oldman=x
print("The Oldest person is:",Oldman)
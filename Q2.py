week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print("Print : ")
for day in week:
    print(day,end=" ")
print("\n")
#append()
print("1. append()")
week.append('Week')
print(week)

#copy()
print("2. copy()")
week2 = week.copy()
print(week2)

#clear()
print("3. clear()")
week2.clear()
print(week2)

#extend()
print("4. extend()")
week2 = ['Week', 'Days']
week.extend(week2)
print(week)

#index()
print("5. index()")
x = week.index('Monday')
print("Index of 'Monday' is ",x)

#count()
print("6. count()")
x = week.count('Sunday')
print("Count of 'Sunday' is ",x)

#insert()
print("7. insert()")
week.insert(0,'Week Days')
print(week)

#pop()
print("8. pop()")
week.pop()
print(week)

# remove()
print("9. remove()")
week.remove('Week Days')
print(week)

#sort()
print("10. sort()")
week.sort()
print(week)

#reverse()
print("11. reverse()")
week.reverse()
print(week)

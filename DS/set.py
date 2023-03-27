# Defining Sets
Days =set(["Sat","Sun","Mon"])
Months={"Jan", "Feb", "Mar"}
print(Days)
print(Months)

##Access Data
for day in Days:
    print(day)
    
# Adding el
Days.add("Tues")
print(Days)

# Deleting el
Days.discard("Sun")
print(Days)

# Union 
Weekends=set(["Sat,Sun"])
week = Days | Weekends
print(week)

# Intersection 
Days2= set(["Mon","Sun","Fri"])
All=Days & Days2

print('Days 1')
print(Days)
print('Days 2')
print(Days2)
print("Union Days and Day2")
print(All)

# Difference
DiffDays = Days -Days2
print(DiffDays)

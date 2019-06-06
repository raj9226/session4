technologies=["AI","Android","Hadoop","JEE"]
technologies[1]="mobile App" #updation/set operation
print(technologies)

print()
del technologies[2]
print(technologies)
print(technologies[2])
print(technologies[0:2])
print(technologies[-2])
print(technologies[-1:-2])

data=[1,2,3,4,5,"John","Jennie","Jim","Jack","Joe","John"]
data.pop(3) #remove on the basis of index
print(data)
data.remove(3) #remove on the basis of matching value
print(data)
data.remove("John")
print(data)


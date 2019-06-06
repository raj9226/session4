data=[10,20,90,80,90]
#lengh=len(data)
#print(lenght)
print(len(data))
print(max(data))
print(min(data))
#iterete in list
for i in range(len(data)):
    print(data[i])
#Enhanced for loop/For-Each loop
for elm in data:
    print(elm)
print("--------------")

print([x**2 for x in data])

print("--------------------")
numbers=list(range(1,101,50))
print(numbers)
print(x//2 for x in numbers)
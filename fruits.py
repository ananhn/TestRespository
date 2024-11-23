fruits = ["apple","banana","cherry","date"]
print(fruits)

numbers = [10,20,30,40,50]
print("First element:",numbers[0])
print("Last element:",numbers[-1])

animals =["cat","dog","bird"]
animals[1] = "hamster"
print(animals)

animals =["cat","dog","bird"]
animals[2]= "rabbit"
print(animals)

colors = []
colors.append("red")
colors.append("green")
colors.append("blue")
colors.remove("green")
print(colors)

names =["Alice","Bob","Charlie","Diana"]
print("Length of the list:",len(names))

numbers = [4,7,1,8,5]
total_sum = sum(numbers)
print("Sum of elements:",total_sum)

ages =[23,45,18,34,60]
print("Maximun age:",max(ages))
print("Minimum age:",min(ages))

scores =[88,56,92,78,61]
scores.sort()
print("Sorted list:",scores)

numbers=[1,3,5,7,9]
if 5 in numbers:
    print("Found")
else:
    print("Not found")

items =[1,2,2,3,4,4,4,5]
count_of_4 = items.count(4)
print("Count of 4:",count_of_4)

list_1= [1,2,3,4,5]
list_2= [6,8,7]
list_1.extend(list_2)
print(list_1)




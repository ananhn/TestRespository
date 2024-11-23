fruits = ["cherry","blueberry","banana","kiwi","orange"]
print(fruits)

colors = ['red','blue','green','yellow','purple']
print("first element:",colors[0])
print("third element:",colors[2])
print("last element:",colors[-1])

numbers = [10,20,30,40,50,]
numbers[1] = "25"
numbers[4] = "60"
print(numbers)

names = ["Alice","Bob","Charlie","David","Emma"]
subset = names[:3]
print(subset)

numbers = list(range(1,11))
for i in numbers:
 print(i**2)

shopping_cart = []
shopping_cart1 = ['butter','cheese']
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
shopping_cart.extend(shopping_cart1)
print(shopping_cart)

numbers = [45,22,88,56,92,33]
print("Maximum number:",max(numbers))
print("Minimum number:",min(numbers))

letters = ['a','b','a','c','b','a','d']
count_of_a = letters.count('a')
print("count of a:",count_of_a)

even_number = [i**2 for i in range(0,11,2)]
print(even_number)

nums =[1,2,2,3,4,4,5,6,6,7]
num_set= set([1,2,2,3,4,4,5,6,6,7])
print(num_set)














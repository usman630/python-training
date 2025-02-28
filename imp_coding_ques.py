

# def reverse_int(n):
#     for i in n:
#         if i[::-1] == i:
#             print(f'{i} is a palindrome ')
#         else:
#             print(f'{i} is not a palindrome')
# res = reverse_int(["oxpxo","usman","loop"])

# def reverse(n):
#     res = ""
#     for i in range(1,n+1):
#         res = str(i) +" "+ res 
#     return res
# res = reverse(10)
# print(res)


# def reverse(n):
#     for i in range(n,0,-1):
#         print(i,end=" ")
# res = reverse(10)

# def reverse(n):
#     for i in range(n):
#         print(n-i, end=" ")
# res = reverse(10)


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def brid(self):
#         print(self.name)

# # single inh
# class Dogson(Dog):
#     def dogson(self):
#         print("Iam dog son")

# # multilevel inh
# class DogGrandSon(Dogson):
#     def dogGrandSon(self):
#         print("Dog Grand Son")


# class Frindely:
#     def Frd(self):
#         print("Iam friendly beard")

# class GoldenRetiver(Dog, Frindely):
#     def Golden(self):
#         print("iam golden")


# a = DogGrandSon("puppy",3)
# a.brid()
# a.dogson()
# a.dogGrandSon()
# print(a.name)


# b = GoldenRetiver("sunny",5)
# b.Frd()
# b.Golden()


# a = [0,1,2]
# a.sort(reverse=True)
# print(a[1])

# find the word which starts with t
# s = "the and tiger and tit and toy"
# a = s.split(" ")
# res = []
# for i in a:
#     if i[:1] == 't':
#         res.append(i)
# for j in res:
#     print(j, end=" ")
# print(res)

# a = 82083
# c = str(a)
# b = len(c)
# res = 0
# for i in c:
#     d = int(i) ** b
#     res = res + d
# if res == a:
#     print("Aramstrong Nmmber")
# else:
#     print("Not")

# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {"message": "Hello, World!"}

# api.add_resource(HelloWorld, '/hello')

# if __name__ == '__main__':
#     app.run(debug=True)

# a = "PINJARI usman basha"
# print(a.swapcase())

# Write a Python code to implement a function to flatten a nested list
# def flatten(nested_list):
#     flat_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list
# print(flatten([1, [2, [3, 4], 5], 6]))


# Write a Python program to find the longest word in a sentence
# res = "The fox jumps over the lazy dog"
# s = res.split(" ")
# max_s = 0
# res = ""
# for i in s:
#     if len(i) > max_s:
#         max_s = len(i)
# for j in s:
#     if len(j) == max_s:
#         res = res + j
# print(res)

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# a = 2
# b = 3
# c = 5
# if a > b and a > c:
#     res = a
# elif b >c:
#     res = b
# else:
#     res = c
# print(res)

# a = "usman"
# b = "basha"
# print(f"{a} {b}")

# Deep and Shallow copy
# import copy
# a = [[1, 2, 3],[4,5]]
# b = copy.copy(a)
# b[0][2] = 99 
# print(b) 
# print(a)

# class InterviewbitEmployee:
#    def __init__(self, emp_name, emp_age):
#        self.emp_name = emp_name
#        self.emp_age = emp_age 
#    def introduce(self):
#        print("Hello I am " + self.emp_name +" " + str(self.emp_age))
#    def us(self):
#         print(f"Hello this is {self.emp_name}")
#    def user(self):
#         print(self.emp_age,self.emp_name)

# emp_1 = InterviewbitEmployee("Mr Employee",23)
# print(emp_1.emp_name)
# emp_1.introduce()
# emp_1.us()
# emp_1.user()


# using generators fibonacci series
# def fib(n):
#     a,b = 0,1
#     while(a < n):
#         yield a
#         a , b = b, a+b
# x = fib(50)
# for i in fib(50):
#     print(i)

# a = {"a":1,"b":2,"c":3}
# b = dict(zip(a.values(),a.keys()))
# print(b)

# a = [1,1,1,2,2,24,5,6,7,7,8,8,9,9,0,0,0,]
# res = {}
# for i in a:
#     res[i] = res.get(i,0)+1

# for i in res.values():
#     print(i, end=" ")
# print(res)

# a = [i for i in "Usman Basha Pinjari" if i.isupper()]
# print(a)

# a = "usman basha"
# b = a.isalpha()
# if b:
#     print("All alphs only")   
# else:
#     print("NO alphs")

    
# name = input("Please enter your name: ")
# if name.isalpha():
#     print("Thank you for entering your name.")
# else:
#     print("Your name should only contain alphabetic characters.")


# counting strings
# q = [1,2,3,4,5,6,7,8,9,9,0]
# a = [0] * 10
# for i in q:
#     a[i] += 1
# print(a)

# nums = [63, 25, 25,8,63,73, 1, 63,8,8]
# r = {}
# for i in nums:
#     if i in r:
#         r[i] += 1
#     else:
#         r[i] = 1
# print(r)

# res = {}
# for i in nums:
#     res[i] = res.get(i,0)+1
# print(res)

# num_count = {}
# for num in nums:
#     if num in num_count:
#         num_count[num] += 1 
#     else:
#         num_count[num] = 1 
# print(num_count)

# result = [num_count[num] for num in nums]
# print(result)

# result = []
# for num in nums:
#     result.append(num_count[num])
# print(result)


# s1 = "Hello"
# s2 = "Hello"
# s3 = "Hello"
# print (id(s1), id(s2), id(s3))
# print (s1 is s2)

# print(ord("U"))

# a = [1, 2, 2, 3, 3, 4, 4,1,0]
# res = {}
# for i in a:
#     res[i] = res.get(i, 0)+1
# print(res)

# example for *args and **kargs 
# def adder(*num):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     print("Sum:",sum)
# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)
# adder(1,2,3,5,6,10)

# def intro(**data):
#     print("\nData type of argument:",type(data))
#     for key, value in data.items():
#         print("{} is {}".format(key,value))

# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# def fib(n):
#     a , b = 0,1
#     res = []
#     for i in range(n):
#         res.append(a)
#         a,b = b , a+b
#     return res
# re = fib(10)
# print(re)

# To find vowles and vowels conunt 
# a = "pavan kalyanou"
# v = ["a","e","i","o","u"]
# res = []
# result = {}
# for i in a:
#     if i in v:
#         res.append(i)
# for i in res:
#     result[i] = result.get(i,0)+1
# print(result)
# print(res)

# from collections import Counter
# a = [1, 2, 2, 3, 3, 4, 4,1,0]
# counts = Counter(a)
# print(counts)
# unique_value = [key for key, count in counts.items() if count == 1]
# print(unique_value)

# a = [1, 2, 2, 3, 3, 4, 4,1,0]
# res = {}
# for i in a:
#     res[i] = res.get(i,0)+1
# for i,j in res.items():
#     if j == 1:
#         print(i)

# def fib(n):
#     a,b =0,1
#     res = []
#     t_count = 0
#     for i in range(2,n):
#         res.append(a)
#         a,b = b, a+b
#     b = res[:11]
#     for j in b:
#         t_count += j
#     return [res, t_count]
# a = fib(15)
# print(a)

# def pan(s):
#     if s[::-1] == s:
#         print("okay")
#     else:
#         print("not okay")
# a = pan("121")


# a = "usman basha"
# b = a.split(" ")
# res = ""
# for word in b:
#     res = word+ " " + res
# print(res)

# usman basha pinjari -------> Usman Basha Pinjari
# def solve(s):
#     a = s.split()
#     res  = ""
#     for word in a:
#         a = word.capitalize()
#         res = res + a + " "
#     return res
# a = solve("usman basha pinjari")
# print(a)

# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# n = 9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# sock_counts = {}
# for sock in ar:
#         sock_counts[sock] = sock_counts.get(sock, 0) + 1
# res = 0
# for i in sock_counts.values():
#     res = res + i //2
# print(res)
# print(sock_counts)


# input_data = {
#     "patients": [
#         {
#             "claims": {
#                 "id": 1,
#                 "name": "John Doe",
#                 "amount": 200.0,
#                 "status": "Approved"
#             }
#         },
#         {
#             "claims": {
#                 "id": 2,
#                 "name": "Jane Smith",
#                 "amount": 350.5,
#                 "status": "Pending"
#             }
#         },
#         {
#             "claims": {
#                 "id": 3,
#                 "name": "Alice Johnson",
#                 "amount": 150.75,
#                 "status": "Denied"
#             }
#         },
#         {
#             "claims": {
#                 "id": 4,
#                 "name": "Robert Brown",
#                 "amount": 500.0,
#                 "status": "Approved"
#             }
#         }
#     ]
# }
# for patient in input_data["patients"]:
#     print(patient["claims"])

# for ids in input_data["patients"]:
#     print(ids["claims"]["id"])

# for status in input_data["patients"]:
#     print(status["claims"]["status"])

# for i in input_data["patients"]:
#     a = i["claims"]["status"]
#     print(a)


# a = 4
# if a % 2 == 0:
#     print("Even Number")
# else:
#     print("Not Even Number")


# r = []
# for i in range(3,100,3):
#     con = str(i)
#     r.append((con))
# print(r)


# a = ["usman","Lokesh","ajay"]
# b = [99,98,89]
# d = [2,4,6]
# c = zip(a,b,d)
# print(list(c))


# a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
# fruits, quantities = zip(*a)
# print(f"Fruits: {fruits}")
# print(f"Quantities: {quantities}")


# particular one word counts in nested list
# def count_a(lst,target):
#     count = 0
#     for char in lst:
#         if isinstance(char,list):
#             count += count_a(char,target)
#         elif target == char:
#             count += 1
#     return count
# list1 = ['a','a','b',['a'],['a','d'],'c','a','d',['a']]
# target = 'd'
# res = count_a(list1,target)
# print(res)


# number of leters in single string 
# name = "usmankhan"
# new_dic = {}
# for char in name:
#     if char in new_dic:
#         new_dic[char] += 1
#     else:
#         new_dic[char] = 1
# print(new_dic)


# fibonacci series
# def fib(n):
#     a,b = 0,1
#     seq = []
#     for i in range(2,n):
#         seq.append(a)
#         a,b = b,a+b
#     return seq
# res = fib(20)
# print(res)


# def fib(n):
#     a,b = 0,1
#     res = []
#     for i in range(2,n):
#         res.append(a)
#         a,b = b, a+b
#     return res
# out = fib(20)
# print(out)


# To find odd numbers using list comp
# a = [i for i in range(10) if i%2 != 0]
# print(a)


# def palindrome(char):
#     a = char[::-1]
#     if a == char:
#         print("Palinidorme")
#     else:
#         print("Not Palindorrms")
# palindrome("ava")


# def fact(nums):
#     res = 1
#     for i in range(1,nums+1):
#         res = res + (i*i)
#     return res        
# print(fact(7))
    

# a = "rgaonization"
# b = a.replace('o','$')
# c = list(a)
# r = ""
# for i in c:
#     if i =="o":
#         q = i.replace("$","o")
#         r = r + q
#     else:
#         r = r + i
# print(r)


# a = "a"
# print(chr(100))


# list_1 = ['X', 'Y', 'Z']  
# list_2 = [11, 22, 33]
# for i in list_1:
#     for j in list_2:
#         print(i, j)
#         if i == 'Y' and j == 33:
#             print('BREAK')  
#             break  
#     else:
#         continue  
#     break   


# a = "usman"
# b = "BA"
# c = b.join(a)
# print(c)


# import numpy as np
# import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid(True)
# plt.show()

# age_input = input("Enter your age: ")

# age = int(age_input)

# if age < 0:
#     print("Please enter a valid age.")
# elif age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# my_tuple = ('sara', 6, 5, 0.97)
# my_list = ['sara', 6, 5, 0.97]
# print(my_tuple[0])     # output => 'sara'
# print(my_list[0])     # output => 'sara'
# my_tuple[0] = 'ansh'    # modifying tuple => throws an error
# my_list[0] = 'ansh'    # modifying list => list modified
# print(my_tuple[0])     # output => 'sara'
# print(my_list[0])


# decorator function to convert to lowercase
# def lowercase_decorator(function):
#    def wrapper():
#        func = function()
#        string_lowercase = func.lower()
#        return string_lowercase
#    return wrapper
# # decorator function to split words
# def splitter_decorator(function):
#    def wrapper():
#        func = function()
#        string_split = func.split()
#        return string_split
#    return wrapper
# @splitter_decorator # this is executed next
# @lowercase_decorator # this is executed first
# def hello():
#    return 'Hello World'
# hello()   # output => [ 'hello' , 'world' ]

# def my_decorator(a):
#     def demo():
#         print("Something before the function.")
#         a()
#         print("Something after the function.")
#     return demo

# @my_decorator
# def say_hello():
#     print("Hello!")

# Call the function
# say_hello()

# def multiply(*zz):
#    mul = 1
#    for num in zz:
#        mul = mul * num
#    return mul
# print(multiply(1, 2, 3, 4, 5,6))


# a = lambda a,b : a*b
# print(a(24,5))

# def lower_convert(function):
#    def demo(name):
#       func  = function(name)
#       a = func.lower()
#       return a
#    return demo

# def sp_con(function):
#    def demo(name):
#       func = function(name)
#       c = func.split()
#       return c
#    return demo

# @sp_con
# @lower_convert
# def hello(name):
#     return(name)

# a = hello("USMAN BASHA PINAJRI")
# print(a)

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         for num in nums:
#             index = abs(num) - 1
#             if nums[index] > 0:
#                 nums[index] = -nums[index]
#         missing_numbers = []
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 missing_numbers.append(i + 1)
#         return missing_numbers


# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & (n-1)) == 0


# Fibonacci Numbers using genaretor
# def fib(limit):
#     a, b = 0, 1
#     while b < limit:
#         yield b
#         a, b = b, a + b
# # Create a generator object
# x = fib(200)
# # Iterate over the generator object and print each value
# for i in x:
#     print(i) 


# def a():
#     def b():
#         return("kjdshjiadfg")
#     return b
# res = a()
# print(res())


# Write a program to count the occurrences of each word in the text given below.
# a = """Through three cheese trees three free fleas flew.
# While these fleas flew, freezy breeze blew.
# Freezy breeze made these three trees freeze.
# Freezy trees made these trees' cheese freeze.
# That's what made these three free fleas sneeze."""
# punctuation = [",", ".", "'"]
# for p in punctuation:
#     a = a.replace(p, "")

# words = a.split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# for word, count in word_count.items():
#     print(f"{word}: {count}")

# def New_func():  
#     print ("Hi, Welcome to JavaTpoint")  
# New_func() 


# generates in python
# def seq(n):
#     for i in range(n):
#         return i
# res =seq(10)
# for q in res:
#     print(q)

# def grepper_gen():
#   yield "add"
#   yield "grepper"
#   yield "answer"
# grepper = grepper_gen()
# next(grepper)
# next(grepper)
# next(grepper)

# s = "HelloWorld!@*"
# print(s[0:14:2])

# STR Softwares Jaipur Rajasthan


# a2b4c3
# from collections import Counter
# a = "aabbbbccc"
# char_count = Counter(a)
# for char, count in char_count.items():
#     print(f"{char}{count}", end="")

# string = "jjdffhnnddnn"
# string2 = ""
# count = 0
# for char in set(string):
#     count = string.count(char)
#     if count>0:
#         string2 += char+str(count)
#     else:
#         string2 += char
# print(string2)

# finding GCD
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# num1 = int(input("enter number1:"))
# num2 = int(input("enter number2:"))
# res = gcd(num1,num2)
# print(res)

# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: ")) 
# gcd = 1 
# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i 
# print(gcd)

# a = 48
# b = 18
# c = ""
# d = ""
# res = ''
# for i in range(1,10):
#     if a%i == 0:
#         c += str(i) 
# for i in range(1,10):
#     if b%i == 0:
#         d += str(i)
# for i in c[::-1]:
#     if i in d:
#         res += str(i)
# print(res[:1])

# import keyword
# print(len(keyword.kwlist))
# print(keyword.kwlist) 


# reverse the word
# str1 = "Analytics Vidhya diva"
# a = str1.split()
# # b = a[::-1]
# c = ""
# for i in a:
#     c= i +" "+ c
# print(c)


# to find greater number
# a = [3,5,6,8,10,19,-1]
# res = 0
# for i in a:
#     if res < i:
#         res = i
# print(res)

# finding factorial of number
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
# res = factorial(5)
# print(res)


# Decorator
# def main(func):
#     def demo():
#         func()
#         print("How are you")
#     return demo

# List Comprehension
# nested_list = [1, 2,3, 4, 5,6]
# even = [i for i in nested_list if i%2 == 0]
# print(even)

# def main2(func):
#     def demo():
#         func()
#         print("Nice to meet you")
#     return demo
# @main2
# @main
# def a():
#     print("Hii usman")
# res = a()


# def calculate_simple_interest(principal, rate, time):
#     simple_interest = (principal * rate * time) / 100
#     return simple_interest
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate (in percentage): "))
# time = float(input("Enter the time period (in years): "))
# interest = calculate_simple_interest(principal, rate, time)
# print(f"The simple interest for the principal amount ${principal}, annual interest rate of {rate}%, and time period of {time} years is ${interest}.")


# finding small number in list
# a = [1,2,3,5,6,7,-2]
# res = a[0]
# for i in a:
#     if i < res:
#         res = i
# print(res)


# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.grid(True)
# plt.show()

# # Plot of the Linear Equation
# x = np.linspace(start=-10, stop = 10, num = 400)
# m = 2  # Slope
# c = 3  # Intercept
# y = m * x + c

# plt.plot(x, y, label='y = 2x + 3')
# plt.title('Plot of the Linear Equation')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.xlim(0,10) # Lower Limit, Upper Limit
# plt.ylim(0,20) # Lower Limit, Upper Limit
# plt.grid(True)  
# plt.show()

# Plot of the Quadratic Equationx
# Define the coefficients
# a = 1
# b = -4
# c = 4

# # Generate x values
# x = np.linspace(-1, 7, 400)

# # Calculate y values using the quadratic equation
# y = a * x**2 + b * x + c

# # Create the plot
# plt.plot(x, y, label='y = x^2 - 4x + 4')

# # Adding title and labels
# plt.title('Plot of the Quadratic Equation')
# plt.xlabel('x')
# plt.ylabel('y')

# plt.xlim(-5,10)
# plt.ylim(0,30)

# plt.legend()
# # Add grid
# plt.grid(True)

# # Show the plot
# plt.show()

# a = np.array([[3,4,5,4],[3,6,5,6],[7,8,9,5]])
# b = a.T
# print(a)
# print(b)

# # arr = np.array((1, 2, 3, 4, 5))

# print(arr)

# import pandas as a

# aa = a.Series([1,2,3,4,5])

# file_path = r"C:\Users\HP\Downloads\industry.csv"

# bb = a.read_csv(file_path)
# print(bb)

# data = {
#   "calories": [420, 380, 390,400],
#   "duration": [50, 40, 45,46],
#   "date":[1,2,3,4]
# }

# df = a.DataFrame(data, index = ["day1", "day2", "day3", "day4"])

# dd = df['calories'].min()
# # print(dd)

# # print(df) 


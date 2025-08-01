#----------------TASK_1---------------#

def odd_numbers(start,end):

    for i in range(start,end+1):
        if i % 2 != 0:
            yield i 

for number in odd_numbers(5, 25):
    print(number)


#----------------TASK_2---------------#

def odd_numbers_2(start,end):
    my_list = [1, 5, 9, 12, 15, 18, 22]
    for i in my_list:
        if i < start or i > end:
             yield i 
            

for number_2 in odd_numbers_2(10, 20):
    print(number_2)


#----------------TASK_3---------------#

def horizontal(symbol):
    t = int(input("How namy times: "))
    print(symbol * t)

def vertical(symbol):
    t = int(input("How namy times: "))
    for _ in range(t):
        print(symbol)

def result(symbol , function_to_call):
    function_to_call(symbol)

symbol = input("Please add your favorite symbol: ")
sign = input("1.horizontal or 2.vertical: ")

if sign == "1":
    result(symbol, horizontal)
elif sign == "2":
    result(symbol, vertical)
else:
    print("PLease add correct info!")

#----------------TASK_4---------------#

import time

odd = []


def measure_time(func):
   def wrapper():
      start = time.time()
      result = func()
      end= time.time()
      print(f"Time taken by function: {end - start} seconds")
      return result
   return wrapper


@measure_time
def odd_numbers():
    for i in range(0,10000):
     if i % 2 == 0:
        odd.append(i)
    return odd

even_list = odd_numbers()
print(even_list)


#----------------TASK_5---------------#

import time


def measure_time(func):
   def wrapper():
      start_time = time.time()
      result = func()
      end_time= time.time()
      print(f"Time taken by function: {end_time - start_time} seconds")
      return result
   return wrapper


@measure_time
def odd_numbers():
    start = int(input("Add your first range: "))
    end = int(input("Add your second range: "))
    odd = []
    for i in range(start,end +1):
     if i % 2 == 0:
        odd.append(i)
    return odd

even_list = odd_numbers()
print(even_list)

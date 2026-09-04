#this is how we create a decorator

import time
# current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        time_taken = end_time - start_time
        return time_taken
    return wrapper_function
  
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
    
print(fast_function())
print(slow_function())
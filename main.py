# import math_functions

# result1 = math_functions.add(5, 3)
# print(result1)  # Output: 8

# result2 = math_functions.subtract(5, 3)
# print(result2)


count = 10  # Global variable

def outer_function():
  count = 5  # Local variable within outer_function

  def inner_function():
    
    nonlocal count  # Local variable within inner_function
    count = 2
    increment = count + 1
    print(f"Inner function: {count+ 1}")  # Accesses local count (2)

  inner_function()
  print(f"Outer function: {count}")  # Accesses local count (5)

print(f"Global scope: {count}")  # Accesses global count (10)

outer_function()

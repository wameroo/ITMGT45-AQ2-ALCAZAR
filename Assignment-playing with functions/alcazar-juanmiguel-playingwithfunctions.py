#!/usr/bin/env python
# coding: utf-8

# ## Playing With Functions

# These exercises are designed to strengthen your grasp on basic programming concepts. Read what is required of you carefully. For example, instructions to **return** values are not the same as those of **printing**.
# 
# Make sure that cells are in **script mode** (not **interactive mode**).
# 

# # 1
# ### 1 point
# 
# Write a function that takes the circumference of a circle as a parameter and **returns** the area of that circle.
# 
# Note: Assume the value of pi is 3.1416

# In[1]:


# 1
# circumference = 2pir
# area = pir^2
# in[] is circumference
def get_radius(circ):
    r = circ/6.2832
    return r



def circ_to_area(circ): 
    r = get_radius(circ)

    area = (3.1416 * r ** 2)
    
    return area

print(circ_to_area(1))
 


# # 2
# ### 2 points
# 
# Write a function that takes a 5-character string as a parameter and **returns** the string in reverse order.
# 
# e.g. reverseString("Hello") -> "olleH"

# In[2]:


# 2

def reverseString(string):
    string = string[0:5]
    string = string[::-1]
    return string

print(reverseString("Hello"))


# # 3
# ### 2 points
# 
# Write a function that takes a positive integer as input and **returns** the sum of all positive integers smaller than and including the number itself.
# 
# e.g. backAddition(5) -> 1 + 2 + 3 + 4 + 5 -> 15

# In[11]:


#  3

def backAddition(var_a):
    var_b = 0
    while var_a > 0:
        var_b = var_b + var_a
        var_a -= 1
    return var_b

print(backAddition(5))


# # 4
# ### 5 points (all or nothing)
# 
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# 
# Show code that generates the answer.

# In[13]:


# 4 

nat_numbers = []

for x in range(0, 101):
    nat_numbers.append(x)
    

def square(number):
    return number ** 2

squaring_map = map(square, nat_numbers)
squared_numbers = list(squaring_map)


answer = (square(sum(nat_numbers))) - (sum(squared_numbers))

print(answer)


# # 5
# ### 5 points 
# 
# Write a function that allows a self-service Point of Sale system to give you the exact change when you pay in cash.
# 
# The function should accept the number of cents entered by the caller of the function. It then should **display** the denominations of the coins that should be given to the buyer. The change should use as few coins as possible. Assume that the Point of Sale system is loaded with 1 cent, 5 cents, 10 cents, 25 cents and 1 peso coins.
# 
# Write main program code that accepts the number of cents manually through user input and calls the function written above.
# 
# **Input:** The program accepts one positive integer, ***cents***, corresponding to the total change to be given by the Point of Sale system.
# 
# **Output:** The number of 1 peso, 25 cents, 10 cents, 5 cents and 1 cent coins respectively. There should be one output per line.
# 
# **Sample Input 1:**  
# 105
# 
# **Sample Output 1**  
# 1  
# 0  
# 0  
# 1  
# 0  
# 
# **Sample Input 2:**  
# 69  
# 
# **Sample Output 2:**  
# 0  
# 2  
# 1  
# 1  
# 4  
# 
# 
# 

# In[26]:


def cents_change():
    
    cents = int(input("cents: "))

    print(cents//100)
    cents = cents % 100
    print(cents//25)
    cents = cents % 25
    print(cents//10)
    cents = cents % 10
    print(cents//5)
    cents = cents % 5
    print(cents//1)

cents_change()


# In[ ]:





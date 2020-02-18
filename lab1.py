"""
Practice with sequences, iteration, and functions
lab1.py
Created Jan 28, 2020
Author: Mihaela

Implementation requirements:
   1. MUST use a for ... in ... loop
   1. Do NOT use list comprehensions
   2. Do NOT use lambda functions
   3. Do NOT call built-in functions or methods that eliminate the use of a
      for loop
   4. Do NOT use for ... in ... range(len(...))
Mihaela
"""


def smaller_than(limit, num_list): # defining a function smaller_than that takes limit and num_list as parameters
    """
    Computes and returns a list of integers from num_list by selecting only
    the integers that are smaller than limit
    limit: integer
    num_list: list of integers
    Returns: list of integers whose values are smaller than limit

    Example
    smaller_than(3, [4, 1, 2, 7]) returns [1, 2]
    """
    result=[]                     # assigning an empty list to result
    for num in nums:              # iterates the loop for each value in the num_list
        if num<a_limit:           # if num is less than a_limit then it enters the loop
            result=result+[num]   # num will be added to result list
    return result                 # returning the result from the function smaller_than


def sum_odd(n):                  # defining a function sum_odd that takes n as parameter
    """
    Adds up all the odd numbers in the sequence 1 to n and returns the sum
    n: positive integer
    Returns: integer

    Example
    sum_odd(3) returns 4
    """

    nums = range(1,n+1)            #sequence of numbers is assigned to variable nums
    sum_odd=0                      # initializing zero to the variable sum_odd
    for num in nums:               # this loop is used to iterate the sequence of integers in nums
        if num%2==1:               # checks the condition if it is true then it executes the next expression
            sum_odd=sum_odd+num    # num will be added to sum_odd
    return sum_odd                 # returning the value sum_odd from the function sum_odd



def get_lengths(sentence):        # defining a function get_lengths
    """
    Finds the length of each word in sentence and accumulates all the length
    values in a list of integers. It then returns the num_list.
    sentence: string of words separated by blank characters
    Returns: list of integers

    Example:
    get_lengths('a happy song') returns [1, 5, 4]
    """
    result=[]                    # assigning an empty list to variable result
    count=0                      # initializing zero to the variable count
    for i in sentence:           # iterates the loop for each character in the sentence
        if i == " ":             # if the character is space then it executes the next expression
          result=result+[count]  # count is added to result and assigned to variable result
          count=0                # making count as zero

        else:                    # other than the above if condition it executes the next expression
          count=count+1          # count is incremented

    num_list=result+[count]      # count is added to a list and assigned to num_list
    return num_list              # returning the num_list from the function get_lengths


# main function
if __name__ == '__main__':
    print('Testing smaller_than()')
    a_limit = 3                                 #assigning a value 3 to variable a_limit
    nums = [4, 1, 2, 7]                         #assigning a list to nums
    result = smaller_than(a_limit, nums)        #function call
    print(result)                               #prints the result
#  test case that returns the original list
    print('test_case to return original list')
    a_limit=9                                   #assigning a value 9 to variable a_limit
    result = smaller_than(a_limit, nums)        #function call
    print(result)                               #prints the result
#  test case that returns an empty list
    print('test_case to return empty list')
    a_limit=0                                  #assigning a value 0 to variable a_limit
    result = smaller_than(a_limit, nums)       #function call
    print(result)                              #prints the result


#   testing_sum_odd
    print('Testing sum_odd()')
    result=sum_odd(3)                       #function call
    print(result)                           #prints the result
#  test case1 for sum_odd()
    print('test_case1_for_sum_odd()')
    result=sum_odd(1)                       #function call
    print(result)                           #prints the result
#  test case2 for sum_odd()
    print('test_case2_for_sum_odd()')
    result=sum_odd(22)                      #function call
    print(result)                           #prints the result


#   Testing get_lengths
    print('Testing get_lengths()')
    sentence='a happy song'
    num_list=get_lengths(sentence)         #function call
    print(num_list)                        #prints the num_list
#   test case1 for get_lengths()
    print('test_case1_for_get_lengths()')
    num_list=get_lengths('This is Snehitha Mamidi')   #function call
    print(num_list)                                   #prints the num_list
#   test case2 for get_lengths()
    print('test_case2_for_get_lengths()')
    num_list=get_lengths('playing games')             #function call
    print(num_list)                                   #prints the num_list

"""
Practice with sequences, iteration, and functions
lab1.py
Created Jan 28, 20202
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


def smaller_than(limit, num_list):
    """
    Computes and returns a list of integers from num_list by selecting only
    the integers that are smaller than limit
    limit: integer
    num_list: list of integers
    Returns: list of integers whose values are smaller than limit

    Example
    smaller_than(3, [4, 1, 2, 7]) returns [1, 2]
    """
    result=[]
    for num in nums:
        if num<a_limit:
            result=result+[num]
    return result


def sum_odd(n):
    """
    Adds up all the odd numbers in the sequence 1 to n and returns the sum
    n: positive integer
    Returns: integer

    Example
    sum_odd(3) returns 4
    """

    nums = range(0,n+1)
    sum_odd=0
    for num in nums:
        if num%2==1:
            sum_odd=sum_odd+num
    return sum_odd



def get_lengths(sentence):
    """
    Finds the length of each word in sentence and accumulates all the length
    values in a list of integers. It then returns the num_list.
    sentence: string of words separated by blank characters
    Returns: list of integers

    Example:
    get_lengths('a happy song') returns [1, 5, 4]
    """
    result=[]
    count=0
    for i in sentence:
        if i == " ":
          result=result+[count]
          count=0

        else:
          count=count+1

    num_list=result+[count]
    return num_list


if __name__ == '__main__':
    print('Testing smaller_than()')
    a_limit = 3
    nums = [4, 1, 2, 7]
    result = smaller_than(a_limit, nums)
    print(result)

# Write a test case that returns the original list
    print('test_case to return original list')
    a_limit=9
    result = smaller_than(a_limit, nums)
    print(result)

# Write a test case that returns an empty list
    print('test_case to return empty list')
    a_limit=0
    result = smaller_than(a_limit, nums)
    print(result)

    print('Testing sum_odd()')
    result=sum_odd(3)
    print(result)

# Write two test cases for sum_odd() that are different than the given
# example.
    print('test_case1_for_sum_odd()')
    result=sum_odd(1)
    print(result)

    print('test_case2_for_sum_odd()')
    result=sum_odd(22)
    print(result)


    print('Testing get_lengths()')
    sentence='a happy song'
    num_list=get_lengths(sentence)
    print(num_list)

    
    # Write two teat cases for get_lengths() that are different than the given
    # example
    print('test_case1_for_get_lengths()')
    num_list=get_lengths('This is Snehitha Mamidi')
    print(num_list)

    print('test_case2_for_get_lengths()')
    num_list=get_lengths('playing games')
    print(num_list)

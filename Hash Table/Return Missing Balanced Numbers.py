# Return Missing Balanced Numbers
# A balanced array would be an array in which each element appears the same number of times.
# Given an array with n elements, return a dictionary with the key as the element and the value as the count of elements needed to balance the given array.
# Signature 
# HashMap<Object, Integer> returnMissingBalancedNumbers(Object[] elements)
# Input 
# Array of mixed elements (integers, strings, etc.)
# Output
# Object with a mixed key, and an integer value
# Examples
# elements: ["a", "b", "abc", "c", "a"]
# output: {"b":1, "abc":1, "c":1}

# elements: [1,3,4,2,1,4,1]
# output: {2:2, 3:2, 4:1}

# elements: [4,5,11,5,6,11]
# output: {4:1,6:1}

import math
from collections import Counter
# Add any extra import statements you may need here


# Add any helper functions you may need here


def return_missing_balanced_numbers(input):
  # Write your code here
  sorted_dict = Counter(input)
  max_frequency = max(sorted_dict.values())
  missingBalanced = {}
  
  for k , v in sorted_dict.items():
    if v < max_frequency:
      
      missingBalanced[k] = max_frequency - v 
    
  
  return missingBalanced

# Method 2 Using dictionary comprehension

  #freq = Counter(input)
  #max_freq = max(freq.values(),default = 0) # If List is empty
  #return {key : max_freq - counts for key, counts in freq.items() if counts < max_freq}
  



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    print(expected)
    print(' Your output: ', end='')
    print(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  
  # Testcase 1 
  input_1 = ['a','b','abc','c','a']
  output_1 = return_missing_balanced_numbers(input_1)
  expected_1 = {'b':1,'abc':1,'c':1}
  check(expected_1, output_1)

  # Testcase 2 
  input_2 = [1,3,4,2,1,4,1]
  output_2 = return_missing_balanced_numbers(input_2)
  expected_2 = {2:2,3:2,4:1}
  check(expected_2, output_2) 
  
  # Testcase 3
  input_3 = [4,5,11,5,6,11]
  output_3 = return_missing_balanced_numbers(input_3)
  expected_3 = {4:1,6:1}
  check(expected_3, output_3)
  
  # Testcase 4
  input_4 = ["x", "y", "x", "y"]
  output_4 = return_missing_balanced_numbers(input_4)
  expected_4 = {}
  check(expected_4, output_4)
  
  
   # Testcase 5
  input_5 = [1, "1", 1, "1", 2]
  output_5 = return_missing_balanced_numbers(input_5)
  expected_5 = {2: 1}
  check(expected_5, output_5)
  
  
  
  # Add your own test cases here
  
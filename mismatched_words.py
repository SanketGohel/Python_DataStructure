# Return Mismatched Words
# Given an input of two strings consisting of english letters (a-z; A-Z) and spaces, complete a function that returns a list containing all the mismatched words (case sensitive) between them.
# You can assume that a word is a group of characters delimited by spaces.
# A mismatched word is a word that is only in one string but not the other.
# Add mismatched words from the first string before you add mismatched words from the second string in the output array.
# Signature 
# static String[] returnMismatched(String str1, String str2)
# Input
# str1: a string
# str2: a string
# Note: You can only expect valid english letters (a-z; A-Z) and spaces.
# Output
# An array containing all words that do not match between str1 and str2.
# Examples
# str1: "Firstly this is the first string"
# str2: "Next is the second string"
# output: ["Firstly", "this", "first", "Next", "second"]

# str1: ""
# str2: ""
# output: []

# str1: ""
# str2: "This is the second string"
# output: ["This","is","the","second","string"]

# str1: "This is the first string" 
# str2: "This is the second string" 
# output: ["first", "second"]

# str1: "This is the first string extra" 
# str2: "This is the second string" 
# output: ["first", "extra", "second"]


import math
from collections import Counter
# # Add any extra import statements you may need here
# # Add any helper functions you may need here




def return_mismatched_words(str1, str2):
  # Write your code here
#   str1 = str1.split()
#   str2 = str2.split()
#   mismatched_words = []
  
#   for word in str1:
#     if word not in str2:
#       mismatched_words.append(word)
      
#   for word in str2:
#     if word not in str1:
#       mismatched_words.append(word)
      
#   return mismatched_words

    # Method 2:  Using Collection.Counter 
    count1 = Counter(str1.split())
    count2 = Counter(str2.split())
    all_words = set(count1.keys()).union(count2.keys())
    
    return sorted([word for word in all_words if count1[word] != count2[word]])
    # Method 2 ENDS:  Using Collection.Counter 

    # Method 3:  Using Set.symmetric_difference()
    # words1 = set(str1.split())
    # words2 = set(str2.split())
    
    # mismatched = words1.symmetric_difference(words2)  # words in either, but not both
    # return sorted(mismatched)
    # Method 3 ENDS:  Using Set.symmetric_difference()
        
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printStringList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printStringList(expected)
    print(' Your output: ', end='')
    printStringList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":
  # Testcase 1
  str1 = "Firstly this is the first string"
  str2 = "Next is the second string" 
  output_1 = return_mismatched_words(str1, str2)
  expected_1 = ["Firstly", "this", "first", "Next", "second"]
  check(expected_1, output_1)

  # Testcase 2
  str1 = "This is the first string"
  str2 = "This is the second string" 
  output_2 = return_mismatched_words(str1, str2)
  expected_2 = ["first", "second"]
  check(expected_2, output_2)
  
  # Testcase 3
  str1 = "This is the first string extra"
  str2 = "This is the second string" 
  output_3 = return_mismatched_words(str1, str2)
  expected_3 = ["first", "extra", "second"]
  check(expected_3, output_3)
  
  # Testcase 4
  str1 = "This is the first text"
  str2 = "This is the second string" 
  output_4 = return_mismatched_words(str1, str2)
  expected_4 = ["first", "text", "second", "string"]
  check(expected_4, output_4)
  
  
  # Add your own test cases here




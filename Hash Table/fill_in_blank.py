import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def fill_in_the_blanks(input_lst):
  # Write your code here
#   lasted_value = []
#   last_seen = None
#   for val in (input_lst):
    
#     if val != None:
#       lasted_value.append(val)
#       last_seen = val
#     else:
#        lasted_value.append(last_seen)
  
#   return lasted_value

    result = input_lst[:]
    n = len(result)

        # Step 1: Forward pass for replacing from next non-null
    for i in range(n - 2, -1, -1):
        if result[i] is None:
            result[i] = result[i + 1]

    return result



#(1,-1,-1)





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
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":

  # Testcase 1
#   input_lst_1 = [1,None,2,3,None,None,5,None]
#   output_1 = fill_in_the_blanks(input_lst_1)
#   expected_1 = [1, 1, 2, 3, 3, 3, 5, 5]
#   check(expected_1, output_1)
  

  # Testcase 2
  input_lst_2 = [None, 8, None]
  output_2 = fill_in_the_blanks(input_lst_2)
  expected_2 = [None, 8, 8]
  check(expected_2, output_2)


  # Testcase 3
#   input_lst_3 = [1,None,2]
#   output_3 = fill_in_the_blanks(input_lst_3)
#   expected_3 = [1, 1, 2]
#   check(expected_3, output_3)
  

#   # Testcase 4
#   input_lst_4 = [5, None, None]
#   output_4 = fill_in_the_blanks(input_lst_4)
#   expected_4 = [5, 5, 5]
#   check(expected_4, output_4)
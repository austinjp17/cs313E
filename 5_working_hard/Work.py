#  File: Work.py
#  Student Name: Austin Palmer
#  Student UT EID: ajp4344

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    
    lines_written = lines_before_coffee
    coffee_num = 0
    marginal_lines = lines_before_coffee
    while marginal_lines > 0:
        coffee_num += 1
        marginal_lines = lines_before_coffee // (prod_loss ** coffee_num)
        lines_written += marginal_lines
    return(lines_written)


# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    
    init_lines = 1
    lines_written = 0
    
    while lines_written < total_lines:
        lines_written = sum_series(init_lines, prod_loss)
        if lines_written < total_lines:
            init_lines += 1
        
    return(init_lines,init_lines)


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(n, k):
    low = 0
    high = n
    cnt = 0
    while low < high:
        # print(f'high: {high}')
        # print(f'low: {low}')
        middle = (low + high) // 2
        # print(f"middle: {middle}")
        lines_written = sum_series(middle, k)
        cnt += 1
        # print(f"Target: {n}")
        # print(f"Result: {lines_written}")
        if(lines_written == n):
            return(middle, cnt)
        elif(lines_written > n):
            high = middle - 1
        else:
            low = middle + 1
        # print("\n---\n")
   
    return middle,cnt


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    # for i in range(0,1):
    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)
        
        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        # print(f"START: {start}\nFINISH: {finish}")
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()

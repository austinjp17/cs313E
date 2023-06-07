#  File: Work.py
#  Student Name:
#  Student UT EID:
#  Partner Name: [DELETE if you did not work with a partner.]
#  Partner UT EID: [DELETE if you did not work with a partner.]

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(total_lines, prod_loss):
    pass
    '''##### ADD CODE HERE #####'''


# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    pass
    '''##### ADD CODE HERE #####'''


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(n, k):
    pass
    '''##### ADD CODE HERE #####'''


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = True
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

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

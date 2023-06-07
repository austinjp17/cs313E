#  File: Spiral.py
#  Student Name: Austin Palmer
#  Student UT EID: ajp4344
import sys


# Input: n
# Output:
def get_dimension(in_data):
    content = in_data.readline()
    dim = int(content.strip())
    return(dim)

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    if(n % 2 == 0):
        n += 1
    spiral = [[0] * n for i in range(n)]
    num = 1
    x_pos = n // 2
    y_pos = n // 2
    spiral[y_pos][x_pos] = num
    
    # 0 = right, 1 = down, 2 = left, 3 = up
    direction = 0  
    steps = 1
    
    while num < n*n:
        for j in range(2):
            for k in range(steps):
                
                #Set pointer direction
                if direction == 0:
                    x_pos += 1
                elif direction == 1:
                    y_pos += 1
                elif direction == 2:
                    x_pos -= 1
                elif direction == 3:
                    y_pos -= 1
                
                num += 1        
                spiral[y_pos][x_pos] = num
                
                #If val == dim*dim then final cell set
                if num == n*n:
                    return spiral
                
            direction += 1
            if (direction == 4):
                direction = 0
        steps += 1
            
        #direction should go 0 -> 1 -> 2 -> 3 -> 0
            
    return(spiral)
    


# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    lines = in_data.readlines()
    lines = [line.strip('\n') for line in lines]
    for line in lines:
        try:
            adj_sum = sum_adjacent_numbers(spiral, int(line))
            print(adj_sum)
        except ValueError:
            print("Invalid data")
            continue
    


# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    adj_sum = 0
    
    # n not present if less than middle most element
    middle = len(spiral) // 2
    if(n < spiral[middle][middle]):
        return(adj_sum)
    
    # Find input in matrix
    for i in range(len(spiral)):
        
        # first row optimizations
        if( i == 0):
            # skip first row if less than first element
            if (n < spiral[i][0]):
                continue
            
            #return 0 if greater than last element of first row
            if(n > spiral[i][len(spiral[i])-1]):
                return(adj_sum)
        
        for j in range(len(spiral[0])):
            if (spiral[i][j] == n):
                # Var initaliziation
                topRow = False
                botRow = False
                leftRow = False
                rightRow = False
                
                # check if on top row
                if(i != 0):
                    adj_sum += spiral[i-1][j]
                else: topRow = True
                
                # check if on bot row
                if(i+1 != len(spiral)):
                    adj_sum += spiral[i+1][j]
                else: botRow = True
                
                # check if on right edge
                if(j+1 != len(spiral)):
                    adj_sum += spiral[i][j+1]
                else: rightRow = True
                
                # check if on left edge
                if(j != 0):
                    adj_sum += spiral[i][j-1]
                else: leftRow = True
                
                # diagonal adjacents
                
                #top left diagonal
                if not topRow and not leftRow:
                    adj_sum += spiral[i-1][j-1]
                    
                #top right diagonal
                if not topRow and not rightRow:
                    adj_sum += spiral[i-1][j+1]
                    
                #bot left diagonal
                if not botRow and not leftRow:
                    adj_sum += spiral[i+1][j-1]
                
                #bot right diagonal
                if not botRow and not rightRow:
                    adj_sum += spiral[i + 1][j + 1]
                
                return(adj_sum) 
                    
                
                


# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin
    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    #print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()

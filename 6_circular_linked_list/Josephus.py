#  File: Josephus.py
#  Student Name: Austin Palmer
#  Student UT EID: ajp4344

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        new_node = Link(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.last.next = self.first


    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        
        #check last node
        if(self.last.data == data):
            return(self.last)
        
        #check all but last node
        pointer = self.first
        while pointer != self.last:
            if pointer.data == data:
                return(pointer)
            else:
                pointer = pointer.next
        
        # if not found
        return(None)
            

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        pointer = self.first

        # IF FIRST ELEMENT
        if (self.first.data == data):
            deleted = self.first
            self.first = pointer.next
            self.last.next = self.first
            return(deleted)
        
        while pointer != self.last:
            if pointer.next.data == data:
                if pointer.next == self.last:
                    self.last = pointer
                deleted = pointer.next
                pointer.next = pointer.next.next
                return(deleted)
            else:
                pointer = pointer.next
        return(None)
        

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        # Q: IS START AN INDEX OR DATA VALUE?
        pointer = self.find(start)

        for i in range(step-1): #STEP OR STEP - 1 ???
            pointer = pointer.next
        deleted = self.delete(pointer.data)

        return(deleted, pointer.next.data)
        
        

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.is_empty():
            return("None")

        str_list = ''
        current = self.first
        while current != self.last:
            str_list += str(current) + ' -> '
            current = current.next
        str_list += str(self.last)
        # return("{} -> {} -> {} -> {} -> ...".format(
        #     str_list, 
        #     str(self.first), 
        #     str(self.first.next),
        #     str(self.first.next.next)
        #     ))
        return(str_list)


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    c_list = CircularList()
    for i in range(1, num_soldiers + 1):
        c_list.insert(i)

    return(c_list)

    # # TESTS
    # print("\n--- INIT LIST ---\n",c_list)

    # # DELETE TEST
    # data_to_delete = 1
    # c_list.delete(data_to_delete)
    # print(f"\n--- DELETE {data_to_delete} ---\n",c_list)

    # data_to_delete = 12
    # c_list.delete(data_to_delete)
    # print(f"\n--- DELETE {data_to_delete} ---\n",c_list)

    # #DELETE AFTER TEST
    # START = 1
    # STEP = 1
    # c_list.delete_after(START,STEP)
    # print(f"\n--- DELETE AFTER ---\nSTART: {START}\nSTEP: {STEP}\n",c_list)


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    while num_soldiers > 1:
        deleted, start_data = my_list.delete_after(start_data, step_count)
        # print(f"--- {num_soldiers} ---")
        print(deleted)
        # print(my_list, "\n")
        num_soldiers-=1
    print(my_list)


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = True
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()

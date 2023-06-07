#  File: DNA.py
#  Student Name: Austin Palmer
#  Student UT EID: ajp4344
import sys


# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
    longest_sequences = []
    
    
    # Find 2 char matches
    for i in range(len(s1)):
        seq_len = 2
        s1_seq = s1[i:i+seq_len]
        for j in range(len(s2)):
            s2_seq = s2[j:j+seq_len]
            
            #If 2 char match, increment until no match
            while (s1_seq == s2_seq):
                longest_sequences.append(s1_seq)
                longest_len = len(max(longest_sequences, key=len))
                
                # Iterate seq length
                seq_len += 1
                
                # Break if index goes beyond string
                if(j+seq_len > len(s2)):
                    break
                
                # Get New Sequences
                s1_seq = s1[i:i+seq_len]
                s2_seq = s2[j:j+seq_len]
                
    longest_sequences = [seq for seq in longest_sequences 
                         if len(seq) == longest_len
                         and (len(seq) > 2)]
    longest_sequences = set(longest_sequences)
    longest_sequences = list(longest_sequences)
    longest_sequences.sort()
    
    
    if(len(longest_sequences) == 0):
        print("\nNo Common Sequence Found")
    else:
        print()
        [print(seq) for seq in longest_sequences]


# Input: list of strings, one string per file input line
# Output: process each pair of DNA strings in the list
def process_lines(lines):
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n").upper()
        
    valid_lines = []
    valid_chars = set(["A", "T", "C", "G"])
    for i in range(len(lines)):
        
        # greater than 80 len check
        if(len(lines[i]) > 80):
            continue
        
        # check if empty str
        if(lines[i] == ""):
            continue
        
        #valid chars check
        line_chars = set(lines[i])
        if(len(line_chars - valid_chars) > 0):
            continue
        
        else: valid_lines.append(lines[i])
            
    #print(valid_lines)
    
    for i in range(0, len(valid_lines) - 1, 2):
        #print("--- " + valid_lines[i] + " , " + valid_lines[i+1] + " ---")
        longest_subsequence(valid_lines[i], valid_lines[i+1])
    

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''
    


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        # in_data = open('autograde/test_cases/test_3.in')
        in_data = open('dna.in')
    else:
        in_data = sys.stdin

    # input will be list of strings, one string per line
    lines = in_data.readlines()

    # process the lines
    process_lines(lines)
    in_data.close()


if __name__ == "__main__":
    main()

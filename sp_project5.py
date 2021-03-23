# ==============================================================================
# Simple DNA Sequences
# PROJECT NUMBER: 5
# DUE DATE: Tuesday 11/19/2019
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# First, read in a DNA sequence from a file, and store it in a Python string
# or list. Note: we will keep our sequences very short, in comparison to DNA
# sequences in real life, to make programming and grading this project simpler.
# Print the sequence you read in, to show the contents read in from the file.
# This is your original DNA sequence.  Provide the user with a menu.
# The menu must allow the user to choose among four operations:
#
# (1) Determine the complement of the original DNA sequence read in, and print
# both the original and the complement in a parallel output format, for ease
# of comparison.
#
# (2) Create 5 random simulated simple mutations in the DNA sequence.
# That is, in 5 positions your program selects pseudo-randomly, insert an "M"
# into the position to replace the A, T, G or C that was previously there.
# Then print both the original and the mutated sequence in parallel output
# format, again, for ease of comparison.
#
# (3) Allow the user to enter a substring that he or she wants to search for in
# the original DNA sequence.  For example, the user might search for a sequence
# such as "AGTCA" and find out where this sequence is located.  In this program,
# you only need to find the first instance of such a substring, and report at
# what index it was located at. If the substring is not found, you must report
# that.
#
# (4) Quit the program. 
#
# INPUT
#
# The input files provided are named dna1.txt, dna2.txt and dna3.txt and
# are available from the course web site. You may also make up your own
# text files to test.  You may assume that data files are not empty, do
# contain one DNA sequence, and do not contain any data errors.  You must
# ask the user to input the filename they wish to use. If the file does
# not open with the filename they entered, keep asking them for a filename
# until the file does open successfully.  
#
# USE OF FUNCTIONS
#
# Part of your grade on this and all future course programming projects will be
# determined by how well you utilize functions, arguments and parameters
# appropriately. 
#
# OUTPUT
#
# The original DNA sequence will be displayed
# For each operation the user selects, be sure to output appropriate
# information.
# Be sure to follow all class style guidelines for all required output
# elements and formatting principles
#
# ASSUMPTIONS
#
# We assume that input data is valid and correctly entered by the user.
# The program is guaranteed to warn user from invalid data entered and
# end program.
# ==============================================================================
import random

def main():
    #CONSTANT VARIABLES
    USERINPUT_1 = 1
    USERINPUT_2 = 2
    USERINPUT_3 = 3
    USERINPUT_4 = 4

    dnaString = getFile()
    userInput = getChoice()

    #while loops until user picks 4 to quit the program
    while userInput != USERINPUT_4:
        #displays the original dna string and displays the comliment dna string
        #when user picks menu option 1
        if userInput == USERINPUT_1:
            print("-=-=-=-=-=-\n\nOriginal  : {}".format(dnaString))
            compliment = getCompliment(dnaString)
            print("Compliment: {}".format(compliment))
            print("")
        #displays the original dna string and displays mutated dna string
        #when user picks menu option 2   
        elif userInput == USERINPUT_2:
            print("-=-=-=-=-=-\n\nOriginal: {}".format(dnaString))
            mutation = getMutation(dnaString)
            print("Mutation: {}".format(mutation))
            print("")
        #displays the original dna string and displays the substring index
        #when user picks menu option 3   
        elif userInput == USERINPUT_3:
            print("-=-=-=-=-=-\n\nOriginal: {}".format(dnaString))
            substring = input("Please enter substring: ")
            substring_index = getSubstring(dnaString, substring)
            print("")
            if substring_index == -1:
                print("Doesn't contain given substring")
            else:
                print("Found at index: ", substring_index)
                print("")
        #error checking        
        else:
            print("Invalid Selection")
            print("")
        userInput = getChoice()
    #end of loop    
    print ('Finished')
            
#gets file and reads the dna string on the file
def getFile():
    
    #set to false until a file is found
    fileFound = False
    #getting users input for file
    userFile = input("\nPlease enter a file name: ")
    print("")
    #error check in a while look to have user continue to write in a file name
    #until user gets a correct file name to read
    while fileFound == False:
        try:
            readFile = open(userFile, 'r') #searches for filename to open
            fileFound = True
        except IOError: #gives error when file not found
            userFile = input("Cannot open filenaem. Enter a new file name: ")
            print("")
    #reads file line
    getString = readFile.readline()
    #strips extra lines
    getString.rstrip("\n")
    print("Original Sequence Read from File: ", getString)

    return getString
    
def getChoice():
    #get user input
    userInput = int(input('\nEnter a number 1-4'
                              + '\n1.  Find the complement of the strand'
                              + '\n2.  Mutate the DNA strand'
                              + '\n3.  Find substrand within the strand'
                              + '\n4.  Quit' + '\nEnter your choice: '))
        
    # While loop for error checking with users input
    while userInput < 1 or userInput > 4:
            userInput = int(input('-=-=-=-=-=-\n'+'\nInvalid Selection\n'
                              + '\nEnter a number 1-4'
                              + '\n1.  Find the complement of the strand'
                              + '\n2.  Mutate the DNA strand'
                              + '\n3.  Find substrand within the strand'
                              + '\n4.  Quit' + '\nEnter your choice: '))
            print ('-=-=-=-=-=-\n')

    return userInput

def getCompliment(dna):
    #empty string to store information
    compliment = ''
    #switches the dna string to their complimentary string
    for ch in dna:
        if ch == 'T':
            compliment += 'A'
        elif ch == 'A':
            compliment += 'T'
        elif ch == 'G':
            compliment += 'C'
        elif ch == 'C':
            compliment += 'G'
            
    return compliment

def getMutation(dna):
    #empty string to store information
    mutation = ''
    dna_size = len(dna)
    #random.sample() takes in the dna string and returns x non-repeating
    #elements from the dna string   
    random_nums = random.sample(range(dna_size), 5)

    #makes dna a list
    dna_list = []
    for ch in dna:
         dna_list.append(ch) #appends the dna list

    for num in random_nums:
         dna_list[num] = 'M' #gets the random numbers in the dna list
                             #and changes their letters to M for mutation

    for ch in dna_list:     
         mutation += ch

    return mutation

def getSubstring(dna, substring):

    #finds substring index
    findSubstring = dna.find(substring)
    return findSubstring
                             

main()


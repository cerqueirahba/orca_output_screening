##This script reads 'Orca' outputs files and create a list of files that terminated normally

#Creating a list with all outputs files
list_of_files = []
import os
for filename in os.listdir():
    if filename.endswith('.out'):
         list_of_files.append(filename)

#Defining a function to diferenciate lists
def diferenciate_lists(list1,list2):
    return list(set(list1) - set(list2))

###Verification of normal termination
normal_termination_list = []
pattern = "ORCA TERMINATED NORMALLY"

#creating a list from the "list_of_files" that terminated normally
for each_file in list_of_files:
    with open(each_file) as current_file:
        for line in current_file:
            if pattern in line:
                normal_termination_list.append(current_file.name)

#creating a list of fail calculations and saving on a txt file
fail_termination_list= diferenciate_lists(list_of_files,normal_termination_list)
file = open("fail.txt", "a")
file.write('Failed the calculation:\n')
file.write(str(fail_termination_list))
file.close()

###Looking for imaginary modes on the files that terminated normally
imaginary_pattern="***imaginary mode***"
imaginary_list=[]

for each_file in normal_termination_list:
    with open(each_file) as current_file:
        for line in current_file:
            if imaginary_pattern in line:
                imaginary_list.append(current_file.name)
imaginary_list=list(dict.fromkeys(imaginary_list))   #removing duplicated itens on the list

#adding the files with imaginary frequency on the fail.txt
file = open("fail.txt", "a")
file.write('\nFiles with imaginary frequencies:\n')
file.write(str(imaginary_list))
file.close()

#creating a list with files that terminated normally and has only real frequencies
real_frequencies_list=diferenciate_lists(normal_termination_list,imaginary_list)

#adding the real frequency files on txt file
file = open("normal_files.txt", "a")
file.write("This files terminated normally and has only real frequencies:\n")
file.write(str(real_frequencies_list))
file.close()

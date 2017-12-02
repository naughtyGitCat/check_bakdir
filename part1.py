# windows
import os
a=0
dict_a = {}
total_dict = {}
with open('./bakdir_list.txt','rt') as file_content:
    while True:
        current_line = file_content.readline()
        if not current_line:                                # if already read all of bak_dir list
            break
        current_line = current_line.strip('\n')             # get a path
        a += 1
        print(a)




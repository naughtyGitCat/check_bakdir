# windows
import os
total_list = ''
with open('./bakdir_list.txt','rt') as file_content:
    while True:
        current_line = file_content.readline()
        if not current_line:                                # if already read all of bak_dir list
            break
        current_line=current_line.strip('\n')

        # os.chdir(current_line)
        current_bak_list = os.listdir(current_line)
        total_list += current_bak_list[-1] + '\n'                 # get the last file ,due to the file name regular,and concat with line break
print(total_list)




# total_list = ''
# with open('./bakdir_list.txt', 'rt') as file_content:
#     for current_line in file_content:
#         print(current_line)
#         os.chdir(current_line)
# print(total_list)


#
# true_line=''
# total_list = ''
# with open('./bakdir_list.txt','rt') as file_content:
#     while True:
#         current_line = file_content.readline()
#         if not current_line:                                # if already read all of bak_dir list
#             break
#         a=current_line
#
#         print(a)
# #         os.chdir(current_line)
# #         current_bak_list = os.listdir()
# #         current_bak_list
# #         total_list += current_bak_list[-1]                  # get the last file ,due to the file name regular
# # print(current_bak_list)
# # print(total_list)

# windows
import os
import time


def timestamp2time(timestamp):
    # 把时间戳转换成python标准日志格式：
    #             (tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
    time_std = time.localtime(timestamp)
    time_human = time.strftime('%Y-%m-%d %H:%M:%S',time_std)
    return time_human
# a=timestamp2time(1511971201.7386703)
# print(a)


def get_max(yyy):                                                # 将所有的数值采集到列表中，使用Max方法获取列表最大值
    temp_t = []
    temp_t.append(yyy)                                           # 这两句等同于下面这句
    # temp_t = [yyy]
    max_t = max(temp_t)
    return max_t


def get_pair(dict_a, key_a):                                       # 取出原字典中某对特定的键值对 ，键值对换后，返回新的词典
    new_dict = {}
    value = dict_a[key_a]
    new_dict[value] = key_a
    return new_dict


def get_pair2(dict_a, key_a):                                     # 取出原字典中某对特定的键值对 ，把时间戳转换成可读性时间,键值对换后，返回新的词典
    new_dict = {}
    value = dict_a[key_a]
    new_dict[value] = timestamp2time(key_a)
    return new_dict


dict_a = {}
total_dict = {}
final_dict = []
with open('./bakdir_list.txt', 'rt') as file_content:
    while True:
        current_line = file_content.readline()
        dict_a = {}
        if not current_line:  # if already read all of bak_dir list
            break
        current_line = current_line.strip('\n')  # get a path
        print(current_line)                                           # 测试读出来的文件地址列表正确性
        ## todo:functionitize the above lines
        # os.chdir(current_line)    pri
        os.chdir(current_line)                       #
        current_bak_list = os.listdir(current_line)  # get the filelist
        #   thoughts:first create a dictionary ,write with  every file's ctime which in current path,key:file,context:ctime)
        # then create a excel,write db[accorded to filename],filename,ctime,filesize
        temp_t = []
        for every_file in current_bak_list:          # 循环获取对上一步中获取到的每一个文件的创建时间
            t = os.path.getmtime(every_file)
            temp_t.append(t)
            dict_a[t] = every_file

        # print(t_max)                                                  # 测试最大值读取正确性
        t_max = max(temp_t)
        # print(temp_t)                                                 # 测试临时列表正确性
        # print(t_max)                                                  # 测试最大值读取正确性
        latest = get_pair2(dict_a, t_max)
        print(latest)
# Coded by Takuro TOKUNAGA
# Last modified: October 1st, 2020

import time
import os

start = time.time()

def file_counter(path, arg_total_file_num):
    files = os.listdir(path)
    count = len(files)

    percentage = count/arg_total_file_num*100

    return print("Progress:{:.2f}".format(percentage) + "[%]")

def remaining(path, arg_total_file_num, arg_speed):
    files = os.listdir(path)
    count = len(files)
    remain_time = (arg_total_file_num-count)/arg_speed # [min], 32 files per min

    return print("Remaining:{:.2f}".format(remain_time) + "[min]")

def comments_input():
    print ("Input >> file per min?")

def begin():
    print ("begin")

def end():
    print ("end")

path_abinit = "/Users/Takuro/codes/enfht/abinit/small_mat_center/general"

# main
begin()
comments_input()
speed_keyboard = input()
speed = int(speed_keyboard)
total_file_num = 6912

file_counter(path_abinit, total_file_num)
remaining(path_abinit, total_file_num, speed)

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")

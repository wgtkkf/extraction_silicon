# overwrite 0 kb text file to zeromatrix
# Coded by Takuro TOKUNAGA
# Last updated Octber 23, 2020

import numpy as np
import pandas as pd
import os
import time

start = time.time()

def comments():
    print ("overwriting..")

def begin():
    print ("begin")

def end():
    print ("end")

# parameters
atom_num = 16

# main
begin()
comments()

path = "../abinit/small_mat_center/"
zero_mat = open(path+"zeromatrix.txt", "r")
contents = zero_mat.read()

# read files
for i in range(-1, 2, 1): # zloop
    for j in range(-1, 2, 1): # xloop
        for k in range(-1, 2, 1): # yloop
            for l in range(0, atom_num): # 0~15
                for m in range(0, atom_num): # 0~15
                    if i==1: # flipped for some reason, originally -1
                        filesize = os.path.getsize(path+"general/si_4_Generic"+str(l+1)+"_Generic"+str(m+1)+"_K10_"+str(j)+str(k)+".txt")
                        if filesize == 0:
                            f1 = open(path+"general/si_4_Generic"+str(l+1)+"_Generic"+str(m+1)+"_K10_"+str(j)+str(k)+".txt", 'w') # write mode
                            f1.write(str(contents))
                            f1.close

                    elif i==0:
                        filesize = os.path.getsize(path+"general/si_4_Generic"+str(l+1)+"_Generic"+str(m+1)+"_K00_"+str(j)+str(k)+".txt")
                        if filesize == 0:
                            f1 = open(path+"general/si_4_Generic"+str(l+1)+"_Generic"+str(m+1)+"_K00_"+str(j)+str(k)+".txt", 'w') # write mode
                            f1.write(str(contents))
                            f1.close
                    else:
                        filesize = os.path.getsize(path+"general/si_4_Generic"+str(l+1)+"_Generic"+str(m+1)+"_K01_"+str(j)+str(k)+".txt")
                        if filesize == 0:
                            f1 = open(path+"general/si_4_Generic"+str(l+1)+"_Generic"+str(m+1)+"_K01_"+str(j)+str(k)+".txt", 'w') # write mode
                            f1.write(str(contents))
                            f1.close

# end
end()

# time display
elapsed_time = time.time()-start
print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")

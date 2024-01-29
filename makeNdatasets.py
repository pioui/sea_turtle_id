import os
import random
import shutil, errno
import numpy as np

def copyallfiles(src, dst):
    files=os.listdir(src)
    for file in files:
        shutil.copy(os.path.join(src,file), os.path.join(dst,file))


data_dir='/ssd_data/ergasies_dsp/pigi/data_shots'
turtles = os.listdir(data_dir)
validation_shot=[None] * len(turtles)
data_cur='/ssd_data/ergasies_dsp/pigi/data'
N=5

for k in range (1,N+1):

    print('#' * 40)
    print('#'*12 +'Random Dataset '+str(k)+'#'*12 )

    if os.path.exists(data_cur):
        os.system('rm -r '+data_cur)
    os.system('mkdir '+data_cur)
    os.system('mkdir '+os.path.join(data_cur,'train'))
    os.system('mkdir '+os.path.join(data_cur,'val'))
    for t in turtles:
        os.system('mkdir '+os.path.join(data_cur,'val',t))
        os.system('mkdir '+os.path.join(data_cur,'train',t))

    print('-' * 10)
    for i in range (0,len(turtles)):
        print("Turtle:",turtles[i])
        shots=os.listdir(os.path.join(data_dir,turtles[i]))
        validation_shot[i] = random.choice(shots)
        print("Validation shot:",validation_shot[i])
        copyallfiles(os.path.join(data_dir,turtles[i],validation_shot[i]),os.path.join(data_cur,'val',turtles[i]))
        for j in range(0,len(shots)):
            if shots[j] != validation_shot[i]:
                copyallfiles(os.path.join(data_dir,turtles[i],shots[j]),os.path.join(data_cur,'train',turtles[i]))
        print('-' * 10)

    os.system('python3 turtles_train_conv.py')
    os.system('python3 turtles_train_ft.py')







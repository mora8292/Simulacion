import numpy as np

bros = np.random.randint(0,9,2)

libreta=[0,0]

print (bros)
if bros[0] == bros[1]:
    libreta[0]+=2
    libreta[1]+=2
elif ((abs(bros[0]-bros[1])) % 2) == 0:
    libreta[0]+=1
else:
    libreta[1]+=1

print (libreta)
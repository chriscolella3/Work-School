import numpy as np

arr = np.array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])


print(arr[1:3,1:])
print ("=========")
print(arr[2])
print ("=========")
print(arr[1,2:])
print ("=========")
print(arr[0:4,0:2])

print(arr[:,0]*3 + arr[:,1]*2 + arr[:,2])
      
      
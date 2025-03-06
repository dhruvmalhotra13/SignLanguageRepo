test=[]
import numpy as np

for i in range(2085):
    test.append(8)
for i in range(2126):
    test.append(5)
for i in range(2179):
    test.append(4)
for i in range(2016):
    test.append(9)
for i in range(2241):
    test.append(1)
for i in range(2116):
    test.append(7)
for i in range(2121):
    test.append(6)
for i in range(2202):
    test.append(3)
for i in range(2233):
    test.append(2)
for i in range(2236):
    test.append(0)
    
test=np.array(test)

np.save('ytrain.npy', test)

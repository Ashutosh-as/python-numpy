Jupyter Notebook
numpy by ashu
Last Checkpoint: 10 hours ago
(autosaved)
Current Kernel Logo
Python 3 
File
New NotebookToggle Dropdown
Open...
Make a Copy...
Save as...
Rename...
Save and Checkpoint
Revert to CheckpointToggle Dropdown
Print Preview
Download asToggle Dropdown
Trusted Notebook
Close and Halt
Edit
View
Insert
Cell
Kernel
Widgets
Help

import numpy as np
a=np.array([1,2,3])
print(a)
[1 2 3]
a=np.zeros([3,4])
print (a)
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
a=np.arange(50,50000,10000)
print(a)
[   50 10050 20050 30050 40050]
#lin space
#np.linspace(startnum,endnum,number of point )
z=np.linspace(2,4,3)
print(z)
[2. 3. 4.]
#filling same no
import numpy as np
c=np.full((3,3),8)
print(c)
[[8 8 8]
 [8 8 8]
 [8 8 8]]
#for filling an array with random no
import numpy as np
a=np.random.random((3,3))
print(a)
[[0.65180931 0.94502923 0.77059132]
 [0.53172012 0.84232399 0.57521094]
 [0.24970615 0.98663457 0.87249497]]
import numpy as np
a=np.array([1,2,3]),([4,5,6]))
print(a)
print(a.shape)
[1 2 3]
(3,)
a=np.arange(24)
#another np.arrange which take the no of points and print from zero to last no
​
print(a)
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
a.size
24
a.shape=(6,4)
print(a.shape[0])
print(a.ndim)
#ndim returns the dimension of array
print(a)
a.dtype
#returns the dtype of an array
6
2
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
dtype('int32')
b= np.linspace(3,6,11)
print(b)
print(b.dtype)
[3.  3.3 3.6 3.9 4.2 4.5 4.8 5.1 5.4 5.7 6. ]
float64
#addition using numpy
import numpy as np
np.sum([10,20])
​
30
a,b,c=10,20,30
np.sum([a,b,c])
60
a=[5,8]
b=[2,3]
print(np.subtract(a,b))
print(np.add(a,b))
[3 5]
[ 7 11]
a=np.array([5,6])
b=np.array([8,9])
print(np.divide([a],[b]))
print(np.multiply([a],[b]))
print(np.cos(a))
print(np.log(a))
[[0.625      0.66666667]]
[[40 54]]
[0.28366219 0.96017029]
[1.60943791 1.79175947]
,
#array comparision
a=[1,2,3]
b=[4,5,6]
np.equal(a,b)
array([False, False, False])
a=[1,2,3]
print(np.sum(a))
print(np.max(a))
print(np.mean(a))
print(np.std(a))
​
6
3
2.0
0.816496580927726
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1:])
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[4 5 6]
 [7 8 9]]
)
#array manipulation
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate([a,b],axis=0))
​
[1 2 3 4 5 6]
np.stack
print(np.stack([a,b],axis=0))
print(np.stack)
[[1 2 3]
 [4 5 6]]
#horizontal stack
import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])
​
print('Horizontal Append:', np.hstack((f, g)))
Horizontal Append: [1 2 3 4 5 6]
## Vertical Stack
import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6])
​
print('Vertical Append:', np.vstack((f, g)))
Vertical Append: [[1 2 3]
 [4 5 6]]
​

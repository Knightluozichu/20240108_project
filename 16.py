# import numpy as np
# print(np.__version__)

import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)

'''
常用函数
'''

arr = np.arange(8).reshape(2,2,2)
arr1 = np.array([
    [[3,3],[3,5]],
    [[3,3],[3,5]],
    ])
# print(arr)
# print()
# print(arr1)
# print()
# print(arr.T)
# print(arr.squeeze())
# # print(np.squeeze(arr,1))
# print()
'''
点积的条件：
一维：a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + ...
二维：点积运算等于矩阵乘法。例如，对于两个二维数组A和B，np.dot(A, B)等于一个新的二维数组，它的每个元素都是A的一行和B的一列的点积。
'''
print(np.dot(arr, arr1).shape)

print()
# arr3 = np.array([1,2,3])
# arr4 = np.array([0,1,2])
# print(np.dot(arr3,arr4))
# print()

arr5 = np.array([[[1,2,1,2],[3,4,2,2]],[[1,2,1,2],[3,4,2,2]],[[1,2,1,2],[3,4,2,2]],[[1,2,1,2],[3,4,2,2]],[[1,2,1,2],[3,4,2,2]],[[1,2,1,2],[3,4,2,2]]])
# arr6 = np.array([[1,0,1],[0,1,1]])
arr6 = np.arange(8).reshape(4,2)
print(arr5.shape)
print(arr6.shape)
print()
# print(np.dot(arr5,arr6))
# print()
'''
在矩阵乘法中，我们将第一个矩阵的行（row）和第二个矩阵的列（column）进行点积运算，以得到结果矩阵的对应元素。
'''
print(np.matmul(arr5,arr6).shape)
print(np.dot(arr5,arr6) == np.matmul(arr5,arr6))

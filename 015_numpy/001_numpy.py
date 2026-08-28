import numpy as np
# numpy daha az yer kaplar daha hızlıdır daha ayrınlıtılıdır daha avantajlıodır daha fazla fonksiyonu vardır daha fazla işlem yapılır
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

# print(type(py_list))     ### <class 'list'>
# print(type(np_array))    ### <class 'numpy.ndarray'>   #### aslında bir matris

py_multi = [[1,2,3], [4,5,6], [7,8,9]]
np_multi = np_array.reshape(3,3)    #### aslında 3,3 lük bir matris

# print(py_list)   ### [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(np_multi)  ### iki boyutlu bir matris olarak listeler
[[1 2 3]
 [4 5 6]
 [7 8 9]]

# print(np_array.ndim) # dimension   ### 1 - bir boyutlu 
# print(np_multi.ndim) # dimension   ### 2 - iki boyutlu 

print(np_array.shape) ### (9,)    - bir boyutlu 
print(np_multi.shape) ### (3, 3)  - iki boyutlu 


# NumPy stands for Numerical Python and it's a fundamental package for scientific computing in Python.
# NumPy has a multidimensional array data structures that can represent vectors and matrices.

# When performing operations on large arrays NumPy can often perform several orders of
# magnitude faster than Python lists

# There are two ways to create numpy arrays
# i) Using numpy's array function to create them other array-like objects such as Python lists.
# ii) Using built-in numpy functions that quickly generate specific types of arrays
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5])    # 1d
print()
print("x = ", x)                 # x =  [1 2 3 4 5]
print()

print("x has dimensions:", x.shape)              # (5,)
print("x is an object of type:", type(x))        # <class 'numpy.ndarray'>
print("The elements in x are of type:", x.dtype) # int32
"""

"""
# We create a rank 2 ndarray that only contains integers
Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# We print Y
print()
print("Y = \n", Y)
print()

# We print information about Y
print("Y has dimensions:", Y.shape)              #Y has dimensions: (4, 3)
print("Y has a total of", Y.size, "elements")    #Y has a total of 12 elements
print("Y is an object of type:", type(Y))        #Y is an object of type: class 'numpy.ndarray'
print("The elements in Y are of type:", Y.dtype) #The elements in Y are of type: int32
"""

# Even though NumPy automatically selects the dtype of the ndarray, NumPy also allows you to specify
# the particular dtype you want to assign to the elements of the ndarray
"""
# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int32)
print()
print('x = ', x)
print()

print('The elements in x are of type:', x.dtype)
"""
# Once you create an ndarray, you may want to save it to a file to be read later or
# to be used by another program
"""
x = np.array([1, 2, 3, 4, 5])

# We save x into the current directory as 
np.save('my_array', x)
"""
# You can load the saved ndarray into a variable by using the load() function
"""
# We load the saved array from our current directory into variable y
y = np.load('my_array.npy')

print()
print('y = ', y)
print()
"""
### Using Built-in Functions to Create ndarrays ###
# The function np.zeros(shape) creates an ndarray full of zeros with the given shape
# The np.zeros() function creates by default an array with dtype float64
"""
X = np.zeros((3,4))                                          ## X =
print()                                                      ## [[ 0. 0. 0. 0.]
print('X = \n', X)                                           ## [ 0. 0. 0. 0.]
print()                                                      ## [ 0. 0. 0. 0.]]

print('X has dimensions:', X.shape)                          ## X has dimensions: (3, 4)
print('X is an object of type:', type(X))                    ## X is an object of type: class 'numpy.ndarray'
print('The elements in X are of type:', X.dtype)             ## The elements in X are of type: float64
"""
# The function np.ones(shape) creates an ndarray full of ones with the given shape
"""
X = np.ones((3,2))                                           ## X =
print()                                                      ## [[ 1. 1.]
print('X = \n', X)                                           ## [ 1. 1.]
print()                                                      ## [ 1. 1.]]

print('X has dimensions:', X.shape)                          ## X has dimensions: (3, 2)
print('X is an object of type:', type(X))                    ## X is an object of type: class 'numpy.ndarray'
print('The elements in X are of type:', X.dtype)             ## The elements in X are of type: float64
"""
# The function np.full(shape, constant) creates an ndarray full of any number we want with the given shape

# The np.full() function creates by default an array with the same data type as the
# constant value used to fill in the array
"""
X = np.full((2,3), 5)                                        ## X =
print()                                                      ## [[5 5 5]
print('X = \n', X)                                           ## [5 5 5]]
print()                                                      
                                      
print('X has dimensions:', X.shape)                          ## X has dimensions: (2, 3)
print('X is an object of type:', type(X))                    ## X is an object of type: class 'numpy.ndarray'
print('The elements in X are of type:', X.dtype)             ## The elements in X are of type: int64
"""
# An Identity matrix is a square matrix that has only 1s in its main diagonal and zeros everywhere else.
# The function np.eye(N) creates a square N x N ndarray corresponding to the Identity matrix
"""
X = np.eye(5)                                                ## [[ 1. 0. 0. 0. 0.]
print()                                                      ## [ 0. 1. 0. 0. 0.]
print('X = \n', X)                                           ## [ 0. 0. 1. 0. 0.]
print()                                                      ## [ 0. 0. 0. 1. 0.]
#                                                            ## [ 0. 0. 0. 0. 1.]]
print('X has dimensions:', X.shape)                          ## X has dimensions: (5, 5)
print('X is an object of type:', type(X))                    ## X is an object of type: class 'numpy.ndarray'
print('The elements in X are of type:', X.dtype)             ## The elements in X are of type: float64
"""
# A diagonal matrix is a square matrix that only has values in its main diagonal
# The function np.diag() creates a square ndarray corresponding to the diagonal matrix
"""
X = np.diag([10,20,30,50])                                   ## [[10 0 0 0]
print()                                                      ## [ 0 20 0 0]
print('X = \n', X)                                           ## [ 0 0 30 0]
print()                                                      ## [ 0 0 0 50]]
"""
# NumPy also allows you to create ndarrays that have evenly spaced values within a given interval
# NumPy's np.arange() function creates one dimensional array of evenly sepaced values within a given interval
# This takes 3 arguments : start, stop, and step

# When only one argument is specified np.arange(stop) uses this as a stop argument
# And generates an array of integers from zero to that integer minus one
"""
x = np.arange(10)
print(x)  # [0 1 2 3 4 5 6 7 8 9]
"""
# When used with two arguments arange uses the first as a start argument and second as stop argument
# The start is inclusive and the stop is exclusive
"""
x = np.arange(4,10)
print(x) # [4 5 6 7 8 9]
"""
# When used with three arguments arange generates an array from the first integer to the
# second minus one evenly spaced by the third
"""
x = np.arange(1, 14, 3) # [1 4 7 10 13]
print(x)
"""
# In the cases where non-integer steps are required, it is usually better to use the function np.linspace()
# The np.linspace(start, stop, N) function returns N evenly spaced numbers over the closed interval
# [start, stop]

# This means that both the start and thestop values are included. We should also note the
# np.linspace() function needs to be called with at least two arguments in the form np.linspace(start,stop).
# In this case, the default number of elements in the specified interval will be N= 50
"""
# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0,25,10)
# x = [ 0. 2.77777778 5.55555556 8.33333333 11.11111111 13.88888889 16.66666667 19.44444444 22.22222222 25. ]
print()
print('x = \n', x)
print()                                                      

print('x has dimensions:', x.shape)                          ## x has dimensions: (10,)            
print('x is an object of type:', type(x))                    ## x is an object of type: class 'numpy.ndarray'
print('The elements in x are of type:', x.dtype)             ## The elements in x are of type: float64
"""
# you can let the endpoint of the interval be excluded (just like in the np.arange() function) by setting the
# keyword endpoint = False in the np.linspace() function
"""
# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25,
# with 25 excluded.
x = np.linspace(0,25,10, endpoint = False)
# x = [ 0. 2.5 5. 7.5 10. 12.5 15. 17.5 20. 22.5]
print()
print('x = ', x)
print()

print('x has dimensions:', x.shape)                          ## x has dimensions: (10,)
print('x is an object of type:', type(x))                    ## x is an object of type: class 'numpy.ndarray'
print('The elements in x are of type:', x.dtype)             ## The elements in x are of type: float64
"""
# So far, we have only used the built-in functions np.arange() and np.linspace() to create rank 1 ndarrays
# However, we can use these functions to create rank 2 ndarrays of any shape by combining them with
# the np.reshape() function
# The np.reshape(ndarray, new_shape) function converts the given ndarray into the specified new_shape
# It is important to note that the new_shape should be compatible with the number of elements in the given ndarray
"""
x = np.arange(20)
# Original x = [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19]
print()                                                      
print('Original x = ', x)                                    
print()                                                      
                                                             
# We reshape x into a 4 x 5 ndarray                          ## Reshaped x =
x = np.reshape(x, (4,5))                                     ## [[ 0 1 2 3 4]  
# print the reshaped x                                       ## [ 5 6 7 8 9]
print()                                                      ## [10 11 12 13 14]
print('Reshaped x = \n', x)                                  ## [15 16 17 18 19]]
print()                                                      
                                                             
print('x has dimensions:', x.shape)                          ## x has dimensions: (4, 5)
print('x is an object of type:', type(x))                    ## x is an object of type: class 'numpy.ndarray'
print('The elements in x are of type:', x.dtype)             ## The elements in x are of type: int32
"""
# some functions can also be applied as methods
"""
Y = np.arange(20).reshape(4, 5)

print()                                                      
print('Y = \n', Y)                                           
print()                                                      

"""
"""
X = np.linspace(0, 50, 10, endpoint=False).reshape(5, 2)     ## [[ 0. 5.]
print()                                                      ## [ 10. 15.]
print("X = \n", X)                                           ## [ 20. 25.]
print()                                                      ## [ 30. 35.]
"""
# Random ndarrays are arrays that contain random numbers
# NumPy offers a variety of random functions to help us create random ndarrays of any shape.

# The np.random.random(shape) function to create an ndarray of the given shape with random floats in the
# half-open interval [0.0, 1.0)
"""
X = np.random.random((3,3))
print()
print('X = \n', X)
print()

print('X has dimensions:', X.shape)                          
print('X is an object of type:', type(X))
print('The elements in x are of type:', X.dtype)
"""
# NumPy also allows us to create ndarrays with random integers within a particular interval
# The function np.random.randint(start, stop, size = shape) creates an ndarray of the given shape with
# random integers in the half-open interval [start, stop)
"""
# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
X = np.random.randint(4,15,size=(3,2))
print()
print('X = \n', X)
print()
"""
####
# NumPy ndarrays are mutable,
# meaning that the elements in ndarrays can be changed after the ndarray has been created
# Elements of an ndarray can be accessed or modified by indexing
"""
x = np.array([1, 2, 3, 4, 5])

print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print('This is First Element in x:', x[0]) 
print('This is Second Element in x:', x[1])
print('This is Fifth (Last) Element in x:', x[4])
print()

# Let's access the same elements with negative indices
print('This is First Element in x:', x[-5])
print('This is Second Element in x:', x[-4])
print('This is Fifth (Last) Element in x:', x[-1])

x[3] = 20

print('Modified:\n x = ', x)
"""
# Similarly, we can also access and modify specific elements of rank 2 ndarrays
# To access elements in rank 2 ndarrays we need to provide 2 indices in the form [row, column]
"""
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

print()
print('X = \n', X)
print()

print('This is (0,0) Element in X:', X[0,0])
print('This is (0,1) Element in X:', X[0,1])
print('This is (2,2) Element in X:', X[2,2])

X[0,0] = 20
print('Modified:\n X = \n', X)
"""
# We can delete elements using the np.delete(ndarray, elements, axis) function
# For rank 1 ndarrays the axis keyword is not required.
# For rank 2 ndarrays, axis = 0 is used to select rows, and axis = 1 is used to select columns

# Delete Operation on 1d:-
""""
x = np.array([1, 2, 3, 4, 5])

print()
print("Original x = ", x)

# We delete the first and last element of x
x = np.delete(x, [0, 4])

# We print x with the first and last element deleted
print()
print("Modified x = ", x)                                    ## [2 3 4]
"""
# Delete Operation on 2d:-
"""
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

print()
print('Original Y = \n', Y)

# We delete the first row of y
w = np.delete(Y, 0, axis=0)                                  

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

# We print w                                                 
print()                                                      ## [[4 5 6]
print('w = \n', w)                                           ## [7 8 9]]

# We print v                                                 ## [[2] 
print()                                                      ## [5]
print('v = \n', v)                                           ## [8]]
"""
# We can append values to ndarrays using the np.append(ndarray, elements, axis) function
# This function appends the given list of elements to ndarray along the specified axis

# Append Operation on 1d:-
"""
x = np.array([1, 2, 3, 4, 5])
print()
print('Original x = ', x)

x = np.append(x, 6)                                          ## [1 2 3 4 5 6]

x = np.append(x, [7,8])                                      ## [1 2 3 4 5 6 7 8]

print()
print('x = ', x)
"""
# Append Operation on 2d:-
"""
Y = np.array([[1,2,3],[4,5,6]])
print()
print('Original Y = \n', Y)

v = np.append(Y, [[7,8,9]], axis=0)

q = np.append(Y,[[9],[10]], axis=1)

print()                                                      ## [[1 2 3]
print('v = \n', v)                                           ## [4 5 6]
                                                             ## [7 8 9]]

print()                                                      ## [[ 1 2 3 9]
print('q = \n', q)                                           ## [ 4 5 6 10]]
"""
# We can insert values to ndarrays using the np.insert(ndarray, index, elements, axis) function.
# This func inserts the given list of elements to ndarray right before the given index along the specified axis

# Insert Operation on 1d:-
"""
x = np.array([1, 2, 5, 6, 7])
print()
print('Original x = ', x)

x = np.insert(x,2,[3,4])                                     ## [1 2 3 4 5 6 7]

print()
print('x = ', x)
"""
# Insert Operation on 2d:-
"""
Y = np.array([[1,2,3],[7,8,9]])                              ## [[1,2,3]
print()                                                      ## [7,8,9]]
print('Original Y = \n', Y)

w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,5, axis=1)

print()                                                      ## [[1,2,3]
print('w = \n', w)                                           ## [4 5 6]
                                                             ## [7,8,9]]

print()                                                      ## [[1 5 2 3]
print('v = \n', v)                                           ## [7 5 8 9]]
"""
# Numpy also allows us stack Numpy arrays on top of each other or side by side
# The stacking is done using either the np.vstack() function for vertical stacking
# Or the np.hstack() function for horizontal stacking
# It is important to note that in order to stack ndarrays, the shape of the ndarrays must match
"""
x = np.array([1, 2])

Y = np.array([[3, 4], [5, 6]])

print()
print("x = ", x)

print()
print("Y = \n", Y)

# We stack x on top of Y
z = np.vstack((x, Y))

# We stack x on the right of Y. We need to reshape x in order to stack it on the right of Y.
w = np.hstack((Y, x.reshape(2, 1)))

print()                                                      ## [[1 2]
print("z = \n", z)                                           ## [3 4]
                                                             ## [5 6]]

print()                                                      ## [[3 4 1]
print("w = \n", w)                                           ## [5 6 2]]
"""
# Slicing ndarrays
# NumPy provides a way to access subsets of ndarrays. This is known as slicing.
# Slicing is performed by combining indices with the colon : symbol inside the square brackets
# ndarray[start:end], ndarray[start:], ndarray[:end] the end index is excluded
"""
X = np.arange(20).reshape(4, 5)                              ## [[ 0 1 2 3 4]
print()                                                      ## [ 5 6 7 8 9]
print('X = \n', X)                                           ## [10 11 12 13 14]
print()                                                      ## [15 16 17 18 19]]

Z = X[1:4,2:5]
## Z =
## [[ 7 8 9]
## [12 13 14]
## [17 18 19]]

print()
print('Z = \n', Z)

Y = X[:3,2:5]
## Y =
## [[ 2 3 4]
## [ 7 8 9]
## [12 13 14]]

print()
print('Y = \n', Y)

v = X[2,:]
## v = [10 11 12 13 14]

print()
print('v = ', v)

q = X[:,2]
## q = [ 2 7 12 17]
print()
print('q = ', q)

# We select all the elements in the 3rd column but return a rank 2 ndarray ## [[ 2]
R = X[:,2:3]                                                               ## [ 7]
print()                                                                    ## [12]
print('R = \n', R)                                                         ## [17]]
"""
# Note that when we perform slices on ndarrays and save them into new variables, as we did above,
# the data is not copied into the new variable
# We say that slicing only creates a view of the original array
# If we make changes in sliced ndarray this will also reflect in the original ndarray

# If we want to create a new Numpy array that contains a copy of the values in the slice
# we need to use Numpy's np.copy(ndarray) function, This function can also be used as a method
# By using the copy command. we are creating a new Numpy array, that is completely independent of the original
"""
X = np.arange(20).reshape(4, 5)
Z = np.copy(X[1:4,2:5])
W = X[1:4,2:5].copy()
"""
# NumPy also offers built-in functions to select specific elements within ndarrays

# The np.diag(ndarray, k=N) function extracts the elements along the diagonal defined by N
# As default is k=0, which refers to the main diagonal
# Values of k > 0 are used to select elements in diagonals above the main diagonal,
# and values of k < 0 are used to select elements in diagonals below the main diagonal
"""
X = np.arange(25).reshape(5, 5)
print('z =', np.diag(X))
print('y =', np.diag(X, k=1))
print('w = ', np.diag(X, k=-1))
"""
# The np.unique(ndarray) function returns the unique elements in the given ndarray
"""
X = np.array([[1,2,3],[5,2,8],[1,2,3]])
print('The unique elements in X are:',np.unique(X))
"""
# Boolean Indexing
# Boolean Indexing allowing us select elements using logical arguments instead of explicit indices
"""
X = np.arange(25).reshape(5, 5)

print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# We use Boolean indexing to assign the elements that are between 10 and 17 the value of -1
X[(X > 10) & (X < 17)] = -1
"""
# NumPy also allows for set operations
# This useful when comparing ndarrays
"""
x = np.array([1,2,3,4,5])

y = np.array([6,7,2,8,4])

print('The elements that are both in x and y:', np.intersect1d(x,y))       ## [2 4]
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))  ## [1 3 5]
print('All the elements of x and y:',np.union1d(x,y))                      ## [1 2 3 4 5 6 7 8]
"""
# We can also sort ndarrays in NumPy
# the sort function can also be used as a method. However,
# there is a big difference on how the data is stored in memory in this case

# When np.sort() is used as a function, it sorts the ndrrays out of place,
# meaning, that it doesn't change the original ndarray being sorted

# However, when you use sort as a method, ndarray.sort() sorts the ndarray in place,
# meaning, that the original array will be changed to the sorted one

# out of place sorting
"""
x = np.random.randint(1,11,size=(10,))

print()
print('Original x = ', x)                                    ## [9 6 4 4 9 4 8 4 4 7]

print()
print('Sorted x (out of place):', np.sort(x))                ## [4 4 4 4 4 6 7 8 9 9]

print()
print('x after sorting:', x)                                 ## [9 6 4 4 9 4 8 4 4 7]
"""
# In place sorting
"""
x = np.random.randint(1,11,size=(10,))

print()
print('Original x = ', x)                                    ## [9 9 8 1 1 4 3 7 2 8]

x.sort()

print()
print('x after sorting:', x)                                 ## [1 1 2 3 4 7 8 8 9 9]
"""
# When sorting rank 2 ndarrays, we need to specify to the np.sort() function
# whether we are sorting by rows or columns
"""
X = np.random.randint(1,11,size=(5,5))

print()
print('Original X = \n', X)
print()

print()
print('X with sorted columns :\n', np.sort(X, axis = 0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))
"""
# Numpy's Arithmetic operations
# Numpy allows element-wise operations, as well as matrix operations
# we can perform basic element-wise operations using arithmetic symbols or functions
"""
x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])
                                                             
print('x + y = ', x + y)                                     ## x + y = [ 6.5 8.5 10.5 12.5]
print('add(x,y) = ', np.add(x,y))                            ## add(x,y) = [ 6.5 8.5 10.5 12.5]
print()
print('x - y = ', x - y)                                     ## x - y = [-4.5 -4.5 -4.5 -4.5]
print('subtract(x,y) = ', np.subtract(x,y))                  ## subtract(x,y) = [-4.5 -4.5 -4.5 -4.5]
print()
print('x * y = ', x * y)                                     ## x * y = [ 5.5 13. 22.5 34. ]
print('multiply(x,y) = ', np.multiply(x,y))                  ## multiply(x,y) = [ 5.5 13. 22.5 34. ]
print()
print('x / y = ', x / y)                                     ## x / y = [ 0.18181818 0.30769231 0.4 0.47058824]
print('divide(x,y) = ', np.divide(x,y))                      #divide(x,y)=[0.18181818 0.30769231 0.4 0.47058824]
"""
# We can also perform the same element-wise arithmetic operations on rank 2 ndarrays
# In order to do these operations the shapes of the ndarrays being operated on,
# must have the same shape or be broadcastable
"""
X = np.array([1,2,3,4]).reshape(2,2)
Y = np.array([5.5,6.5,7.5,8.5]).reshape(2,2)

print('X + Y = \n', X + Y)                                    ## [[ 6.5 8.5]
print()                                                       ## [ 10.5 12.5]]
print('add(X,Y) = \n', np.add(X,Y))
print()
print('X - Y = \n', X - Y)                                    ## [[-4.5 -4.5]
print()                                                       ## [-4.5 -4.5]]
print('subtract(X,Y) = \n', np.subtract(X,Y))
print()
print('X * Y = \n', X * Y)                                    ## [[ 5.5 13. ]
print()                                                       ## [ 22.5 34. ]]
print('multiply(X,Y) = \n', np.multiply(X,Y))
print()
print('X / Y = \n', X / Y)                                    ## [[ 0.18181818 0.30769231]
print()                                                       ## [ 0.4 0.47058824]]
print('divide(X,Y) = \n', np.divide(X,Y))
"""
# We can also apply mathematical functions, such as sqrt(x), to all elements of an ndarray at once
"""
x = np.array([1,2,3,4])

# We print x
print()
print('x = ', x)

print()
print('EXP(x) =', np.exp(x))                           ## EXP(x)=[ 2.71828183 7.3890561 20.08553692 54.59815003]
print()                                                 
print('SQRT(x) =',np.sqrt(x))                          ## SQRT(x) = [ 1. 1.41421356 1.73205081 2.]
print()
print('POW(x,2) =',np.power(x,2))                      ## POW(x,2) = [ 1 4 9 16]
"""
# Another great feature of NumPy is that it has a wide variety of statistical functions.
# Statistical functions provide us with statistical information about the elements in an ndarray
"""
X = np.array([[1,2], [3,4]])

print('Average of all elements in X:', X.mean())                                ## X: 2.5
print('Average of all elements in the columns of X:', X.mean(axis=0))           ## X: [ 2. 3.]
print('Average of all elements in the rows of X:', X.mean(axis=1))              ## X: [ 1.5 3.5]
print()
print('Sum of all elements in X:', X.sum())                                     ## X: 10
print('Sum of all elements in the columns of X:', X.sum(axis=0))                ## X: [4 6]
print('Sum of all elements in the rows of X:', X.sum(axis=1))                   ## X: [3 7]
print()
print('Standard Deviation of all elements in X:', X.std())                      ## X: 1.11803398875
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0)) ## X: [ 1. 1.]
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))    ## X: [ 0.5 0.5]
print()
print('Median of all elements in X:', np.median(X))                             ## X: 2.5
print('Median of all elements in the columns of X:', np.median(X,axis=0))       ## X: [ 2. 3.]
print('Median of all elements in the rows of X:', np.median(X,axis=1))          ## X: [ 1.5 3.5]
print()
print('Maximum value of all elements in X:', X.max())                           ## X: 4
print('Maximum value of all elements in the columns of X:', X.max(axis=0))      ## X: [3 4]
print('Maximum value of all elements in the rows of X:', X.max(axis=1))         ## X: [2 4] 
print()
print('Minimum value of all elements in X:', X.min())                           ## X: 1
print('Minimum value of all elements in the columns of X:', X.min(axis=0))      ## X: [1 2]
print('Minimum value of all elements in the rows of X:', X.min(axis=1))         ## X: [1 3]
"""
# NumPy can add single numbers to all the elements of an ndarray without the use of complicated loops
"""
X = np.array([[1,2], [3,4]])

print('3 * X = \n', 3 * X)         ## [[ 3 6]
print()                            ## [ 9 12]]

print('3 + X = \n', 3 + X)         ## [[4 5]        
print()                            ## [6 7]]

print('X - 3 = \n', X - 3)         ## [[-2 -1] 
print()                            ## [ 0 1]]

print('X / 3 = \n', X / 3)         ## [[ 0.33333333 0.66666667]
print()                            ## [ 1. 1.33333333]]
"""
# In the examples above, NumPy is working behind the scenes to broadcast 3 along
# the ndarray so that they have the same shape

# Subject to certain constraints, Numpy can do the same for two ndarrays of different shapes
"""
x = np.array([1,2,3])

Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

Z = np.array([1,2,3]).reshape(3,1)

print('x + Y = \n', x + Y)              ## [[ 2 4 6]
print()                                 ## [ 5 7 9]
                                        ## [ 8 10 12]]

print('Z + Y = \n',Z + Y)               ## [[ 2 3 4]
print()                                 ## [ 6 7 8]
                                        ## [10 11 12]]
"""
# As before, NumPy is able to add 1 x 3 and 3 x 1 ndarrays to 3 x 3 ndarrays by broadcasting
# the smaller ndarrays along the big ndarray so that they have compatible shapes

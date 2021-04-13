# Pandas is a package for data manipulation and analysis in Python
# Pandas incorporates two additional data structures into Python, namely Pandas Series and Pandas DataFrame

## Creating Pandas Series ##

# Pandas series is a one-dimensional array-like object that can hold many data types,such as numbers or strings

# One of the main differences between Pandas Series and NumPy ndarrays is that you can assign an index label to
# each element in the Pandas Series
# In other words, you can name the indices of your Pandas Series anything you want

# Another difference between Pandas Series and NumPy ndarrays is that Pandas Series can hold
# data of different data types

# You can import Pandas by typing:- import pandas as pd
# You can create Pandas Series by using the command pd.Series(data, index),
# where index is a list of index labels
"""
import pandas as pd

# We create a Pandas Series that stores a grocery list                   ## eggs    30
groceries = pd.Series(                                                   ## apples  6
    data=[30, 6, "Yes", "No"], index=["eggs", "apples", "milk", "bread"] ## milk    Yes
)                                                                        ## bread   No
print(groceries)                                                         ## dtype: Object

# We print some information about Groceries
print('Groceries has shape:', groceries.shape)                           ## (4,)
print('Groceries has dimension:', groceries.ndim)                        ## 1
print('Groceries has a total of', groceries.size, 'elements')            ## 4 elements

# We print the index and data of Groceries
print('The data in Groceries is:', groceries.values) #[30 6 'Yes' 'No']
print('The index of Groceries is:', groceries.index) #Index(['eggs', 'apples', 'milk', 'bread'], dtype='object')

# If you are dealing with a very large Pandas Series and if you are not sure whether an index label exists, 
# you can check by using the in command

x = 'bananas' in groceries

y = 'bread' in groceries

print('Is bananas an index label in Groceries:', x) # False
print('Is bread an index label in Groceries:', y)   # True
"""
# Accessing Elements in Pandas Series
# Pandas Series have two attributes, .loc and .iloc to explicitly state what we mean
# The attribute .loc stands for location and it is used to explicitly state that we are using a labeled index

# The attribute .iloc stands for integer location and it is used to explicitly state
# that we are using a numerical index
"""
print('How many eggs do we need to buy:', groceries['eggs'])  ## 30
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']])  ## milk    Yes
print()                                                              ## bread   No
                                                                     ## dtype: object
# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']]) ## eggs   30
print()                                                                                   ## apples 6
                                                                                          ## dtype: object
# We access elements in Groceries using numerical indices:
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) ## eggs   30
print()                                                                    ## apples 6
                                                                           ## dtype: object
# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]]) ## bread  No
print()                                       ## dtype: object

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0]) ## 30
print()                                                    
                                                              ## milk   Yes
# we use iloc to access multiple numerical indices            ## bread  No
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]]) ## dtype: object
"""
# Pandas Series are also mutable like NumPy ndarrays, which means we can change the elements of a
# Pandas Series after it has been created
"""
print('Original Grocery List:\n', groceries)

groceries['eggs'] = 2

print()
print('Modified Grocery List:\n', groceries)
"""
# The Series.drop(label) method removes the given label from the given Series
# Note that the Series.drop(label) method drops elements from the Series out of place
# meaning that it doesn't change the original Series being modified
"""
print('Original Grocery List:\n', groceries)
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact
print()
print('Grocery List after removing apples out of place:\n', groceries)
"""
# We can delete items from a Pandas Series in place by setting the keyword inplace to True in the .drop() method
"""
print('Original Grocery List:\n', groceries)

groceries.drop('apples', inplace = True)

# When we remove elements in place the original Series its modifiedprint()
print('Grocery List after removing apples in place:\n', groceries)
"""
# Just like with NumPy ndarrays, we can perform element-wise arithmetic operations on Pandas Series.
"""
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])
print('Original grocery list of fruits:\n ', fruits)
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2 
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()
"""
# You can also apply mathematical functions from NumPy, such as sqrt(x), to all elements of a Pandas Series
"""
import numpy as np

print('Original grocery list of fruits:\n', fruits)

# We apply different mathematical functions to all elements of fruits
print()
print('EXP(X) = \n', np.exp(fruits))
print() 
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n',np.power(fruits,2))
"""
# Pandas also allows us to only apply arithmetic operations on selected items in our fruits grocery list
"""
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)
"""
## Creating Pandas DataFrames ##

# Pandas DataFrames are two-dimensional data structures with labeled rows and columns,
# that can hold many data types

# We can create Pandas DataFrames manually or by loading data from a file

# We will start by creating a DataFrame manually from a dictionary of Pandas Series
# In this case the first step is to create the dictionary of Pandas Series
# After the dictionary is created we can then pass the dictionary to the pd.DataFrame() function
"""
items = {                                                                    ##         Bob     Alice 
    "Bob": pd.Series(data=[245, 25, 55], index=["bike", "pants", "watch"]),  ## bike    245.0   500.0
    "Alice": pd.Series(                                                      ## book    NaN     40.0
        data=[40, 110, 500, 45], index=["book", "glasses", "bike", "pants"]  ## glasses NaN     110.0
    ),                                                                       ## pants   25.0    45.0
}                                                                            ## watch   55.0    NaN

shopping_carts = pd.DataFrame(items)

print(shopping_carts)

print('shopping_carts has shape:', shopping_carts.shape)  ## (5, 2)
print('shopping_carts has dimension:', shopping_carts.ndim)  ## 2
print('shopping_carts has a total of:', shopping_carts.size, 'elements')  ##10 elements
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
## [[245. 500.]]
## [ nan 40.]
## [ nan 110.]
## [ 25. 45.]
## [ 55. nan]
print('The row index in shopping_carts is:', shopping_carts.index)
## Index(['bike', 'book', 'glasses', 'pants', 'watch'], dtype='object')
print() 
print('The column index in shopping_carts is:', shopping_carts.columns) #Index(['Alice', 'Bob'], dtype='object')
"""
# The row labels of the DataFrame are built from the union of the index labels of the Pandas Series
# we used to construct the dictionary

# And the column labels of the DataFrame are taken from the keys of the dictionary

# NaN stands for Not a Number, and is Pandas way of indicating that it doesn't have a value for that
# particular row and column index

# Pandas allows us to select which data we want to put into our DataFrame by means of the
# keywords columns and index
""" 
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])
##          Alice
## glasses  110
## bike     500
print(alice_sel_shopping_cart)
"""
# You can also manually create DataFrames from a dictionary of lists (arrays)
# we start by creating the dictionary and then passing the dictionary to the pd.DataFrame() function
# We can put labels to the row index by using the index keyword in the pd.DataFrame() function
"""
data = {'Integers' : [1,2,3],                                       ##          Integers    Floats
        'Floats' : [4.5, 8.2, 9.6]}                                 ## label 1      1       4.5
                                                                    ## label 2      2       8.2
# We create a DataFrame and provide the row index                   ## label 3      3       9.6
df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])

print(df)
"""
# Another way of manually creating Pandas DataFrames is by using a list of Python dictionaries
"""
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

print(store_items)
"""
# Accessing Elements in Pandas DataFrames
"""
print(store_items)

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
"""
# It is important to know that when accessing individual elements in a DataFrame, as we did in the last example
# above,the labels should always be provided with the column label first,i.e. in the form dataframe[column][row]

# We can also modify our DataFrames by adding rows or columns
"""
# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
store_items['shirts'] = [15,2]

print(store_items)
"""
# We can also add new columns to our DataFrame by using arithmetic operations
# between other columns in our DataFrame
"""
# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['pants'] + store_items['shirts']

print(store_items)
"""
# To add rows to our DataFrame we first have to create a new Dataframe and then
# append it to the original DataFrame using the .append() method
"""
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3'])

print(new_store)

store_items = store_items.append(new_store)

# We display the modified DataFrame
print(store_items)
"""
# The dataframe.insert(loc,label,data) method allows us to insert a new column in the dataframe
# at location loc, with the given column label, and given data
"""
# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

print(store_items)
"""
# The .pop() method only allows us to delete columns,
# while the .drop() method can be used to delete both rows and columns by use of the axis keyword
"""
store_items.pop('watches')
print(store_items)

store_items = store_items.drop(['shoes'], axis = 1)
print(store_items)

store_items = store_items.drop(['store 2', 'store 1'], axis = 0)
print(store_items)
"""
# The .rename() method alloes us to change the row and column labels
"""
# We change the column label bikes to hats
store_items = store_items.rename(columns = {'bikes': 'hats'})

print(store_items)

# We change the row label from store 3 to last store
store_items = store_items.rename(index = {'store 3': 'last store'})

print(store_items)
"""
# You can also change the index to be one of the columns in the DataFrame
"""
store_items = store_items.set_index('pants')

print(store_items)
"""
# Dealing with NaN
# the .isnull() method returns a Boolean DataFrame and indicates with True the elements that have
# NaN values and with False the elements that are not
"""
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

print(store_items)

# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

print('Number of NaN values in our DataFrame:', x)

# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())
"""
# The .dropna(axis) method eliminates any rows with NaN values when axis = 0
# and will eliminate any columns with NaN values when axis = 1 is used
"""
# We drop any rows with NaN values
store_items.dropna(axis = 0)

# We drop any columns with NaN values
store_items.dropna(axis = 1)
"""
# the .dropna() method eliminates (drops) the rows or columns with NaN values out of place
# You can always remove the desired rows or columns in place by setting the
# keyword inplace = True inside the dropna() func

# Now, instead of eliminating NaN values, we can replace them with suitable values
# We can do this by using the .fillna() method, the .fillna() method replaces the NaN values out of place
# You can always replace the NaN values in place by setting the keyword inplace = True inside the fillna() func
"""
# We replace all NaN values with 0
store_items.fillna(0)
"""
# We can also use the .fillna() method to replace NaN values with previous values in the DataFrame,
# this is known as forward filling .fillna(method = 'ffill', axis)
# When replacing NaN values with forward filling, we can use previous values taken from columns or rows
"""
# We replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)

# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)
"""
# Similarly, you can choose to replace the NaN values with the values that go after them in the DataFrame,
# this is known as backward filling .fillna(method = 'backfill', axis)
"""
# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)

# We replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)
"""
# .interpolate(method = 'linear', axis) method will use linear interpolation to replace NaN values
# using the values along the given axis
"""
# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)
"""
## Loading Data into a pandas DataFrame ##
# Pandas allows us to load databases of different formats into DataFrames
# We can load CSV files into Pandas DataFrames using the pd.read_csv() function
"""
Google_stock = pd.read_csv("./GOOG.csv")

# We print some information about Google_stock
print("Google_stock is of type:", type(Google_stock))
print("Google_stock has shape:", Google_stock.shape)
print(Google_stock)
"""
# We can take a look at the first 5 rows of data using the .head() method
# And last 5 rows of data by using the .tail() method
# We can also optionally use .head(N) or .tail(N) to display the first and last N rows of data, respectively
"""
print(Google_stock.head())

print(Google_stock.tail())
"""
# To check weather we have NaN values in our data set we use the .isnull() method followed by the
# .any() method to check whether any of the columns contain NaN values
"""
Google_stock.isnull().any()
"""
# Pandas provides the .describe() method to get descriptive statistics on each column of the DataFrame
"""
# We get descriptive statistics on our stock data
Google_stock.describe()

# We get descriptive statistics on a single column of our DataFrame
Google_stock['Adj Close'].describe()
"""
# You can also look at one statistic by using one of the many statistical functions Pandas provides
"""
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())
"""
# Data correlation can tell us, for example, if the data in different columns are correlated
# A correlation value of 1 tells us there is a high correlation and a correlation of 0 tells us that
# the data is not correlated at all
"""
# We display the correlation between columns
Google_stock.corr()
"""
# The .groupby() method allows us to group data in different ways
"""
data = pd.read_csv("./fake_company.csv")

print(data)
# We display the total amount of money spent in salaries each year
print(data.groupby(["Year"])["Salary"].sum())

# We display the average salary per year
print(data.groupby(["Year"])["Salary"].mean())

# We display the total salary each employee received in all the years they worked for the company
print(data.groupby(["Name"])["Salary"].sum())

# We display the salary distribution per department per year.
print(data.groupby(["Year", "Department"])["Salary"].sum())
"""

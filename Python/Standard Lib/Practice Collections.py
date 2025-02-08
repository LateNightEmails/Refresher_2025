my_list = [ 1,2, 3, 4, 5]
print( my_list)

# empty list
my_list= []

# list with itegres 
my_list = [ 1,2,3 ,4,5]


# list with mixed data types 
my_list= [ 1, 'bob' , 3.14 , [ 'a' , 24]]


# Cycle through all the elements of a list
for i , z in enumerate(my_list):
    print( i , z)

# find the size of the list
print(len(my_list))

# print the entire list
print(my_list)

# Print data type of object
print(type(my_list))


# init a new list
you_list = list()

# assign value to a list
you_list = my_list

# update original list
my_list[0]= '7777'


# make an evaluation function to save time/typing
def ShowLists():
    print(my_list)
    print(you_list)
    print(my_list==you_list)

# chekc the lists
ShowLists()

# run copy of list to init a new separate list
you_list = my_list.copy()

# update original list
my_list[0]= '88888'

# show the lists
ShowLists()



# place holder for more advanced list operations
if( __name__=="__main__"):
    print("complete")


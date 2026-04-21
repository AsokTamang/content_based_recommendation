import numpy as np
#this function is used for creating a matrix containing new users data in the form of vector, and this matrix matches the shape of the item vector
def gen_newuser_data(new_user,num_items):
    return np.tile(new_user,(num_items, 1))  #here we are making a matrix where the new_user's vector is repeated num_items times in the form of row and just 1 time as the column


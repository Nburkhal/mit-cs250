'''
write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary
'''
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values = 0
    for i in aDict:
        values += len(aDict[i])
    return values


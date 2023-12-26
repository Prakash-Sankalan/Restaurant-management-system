def disc(x):
    '''
    Parameters
    ----------
    x : INT
        Takes total amount as arguement
    Returns Discounted value
    '''
    if x>=5000:
        y=0.2*x
        return x-y
    elif x<5000 and x>2000:
        y=0.15*x
        return x-y
    elif x<2000:
        y=0.05*x
        return x-y
def menu(x):
    '''
    Parameters
    ----------
    x : LIST
        Takes a list of tuples and iterates through it unpacking the tuple
    Returns unpacked tuples
    -------
    '''
    for z in range(len(x)):
        print(*x[z])
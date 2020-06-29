def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    l =[]
    for pos in range(len(aTup)):
        if pos%2 ==0:
            l.append(aTup[pos])
    return tuple(l)

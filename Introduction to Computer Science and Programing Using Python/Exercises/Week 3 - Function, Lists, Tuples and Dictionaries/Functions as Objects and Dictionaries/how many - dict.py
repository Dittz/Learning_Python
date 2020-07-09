animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)


def how_many(aDict):
    count = 0
    for value in aDict.values():
        for item in value:
            count+=1
    print(count)
    return(count)



how_many(animals)

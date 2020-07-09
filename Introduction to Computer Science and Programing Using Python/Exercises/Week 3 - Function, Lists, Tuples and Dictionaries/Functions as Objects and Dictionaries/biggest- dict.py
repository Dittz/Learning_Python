animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)


def biggest(aDict):
    biggest = ''
    biggest_value = 0
    for k, v in aDict.items():
        if len(v) > biggest_value:
            biggest = k
    return(biggest)



biggest(animals)

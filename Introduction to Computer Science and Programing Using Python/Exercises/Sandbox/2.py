'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
'''
s = 'azcbobobegghbob'

count = 0
for pos in range(len(s)-2):
    word = s[pos] + s[pos+1] + s[pos+2]
    if word == 'bob':
        count+=1
print('Number of times bob occurs is {}'.format(count))

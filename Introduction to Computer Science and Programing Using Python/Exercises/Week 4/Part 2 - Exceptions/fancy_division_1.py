def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("o") #raises an exception aways. If another exception is not present this will be printed
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as text: #prints only the text of the exception and not the type of exception
        print(text)

fancy_divide([0, 2, 4], 0)



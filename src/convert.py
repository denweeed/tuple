def convert_string(d: tuple, delim: str = ", ") -> str:
    return delim.join(d)


if __name__ == '__main__':
    tuple1 = ('1', '7', '3', '4', '5', '5', '5', '4', '2',)
    str1 = convert_string(tuple1)
    print(str1)

''' The function convert_string is used to convert a tuple to a string
    Parameters
    ----------
    delim : str, optional
            separator
'''
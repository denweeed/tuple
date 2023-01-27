import typing


def f(t: tuple, elem: typing.Any):
    """"This function displays the element by its number in the tuple
    """
    return t.index(elem)


if __name__ == '__main__':
    tuple1 = ('1', '7', '3', '4', '5', '5', '5', '4', '2',)

    num = str(input("Enter number: "))

    if num in tuple1:
        num = tuple1.index(num)
        print("element number = ", num + 1)
    else:
        num = -1
        print("Wrong element.")

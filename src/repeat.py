from collections import Counter


def repeat():
    return [k for k, v in Counter(d).items() if v > 1]


if __name__ == '__main__':
    tuple1 = ('1', '7', '3', '4', '5', '5', '5', '4', '2',)
    s = repeat(tuple1)

    print(s)

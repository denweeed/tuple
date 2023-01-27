from collections import Counter

if __name__ == '__main__':

    tuple1 = ('1', '7', '3', '4', '5', '5', '5', '4', '2',)

    counts = Counter(tuple1)
    for key, value in counts.items():
        print(key, value)

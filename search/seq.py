def search_seq(data, key):
    data[0] = key
    for i in range(len(data) - 1, 0, -1):
        if data[i] == data[0]:
            return i
        pass


if __name__ == '__main__':
    data = [1, 3, 4, 5]
    print(search_seq(data, 4))
    pass

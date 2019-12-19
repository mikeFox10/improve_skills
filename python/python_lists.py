if __name__ == '__main__':
    N = int(input())
    res = []
    for i in range(N):
        line = input().split()
        if line[0] == 'insert':
            res.insert(int(line[1]), int(line[2]))
        elif line[0] == 'print':
            print(res)
        elif line[0] == 'remove':
            res.remove(int(line[1]))
        elif line[0] == 'append':
            res.append(int(line[1]))
        elif line[0] == 'sort':
            res.sort()
        elif line[0] == 'pop':
            res.pop()
        elif line[0] == 'reverse':
            res.reverse()
        else:
            pass



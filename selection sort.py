# [5, 64, 89, 1, 6]

def selection(l):
    l2 = []
    for i in range(len(l)):
        _min = l[i]

        for j in range(i+1, len(l)):
            if _min > l[j]:
                (_min, l[j]) = (l[j], _min)

            else:
                continue
        l2.append(_min)
    print(l2)


print(selection([5, 64, 89, 1, 6, 100, 74, 2]))
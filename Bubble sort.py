
def bubble(l):
    swapped = False
    l2 = []

    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                (l[j], l[j+1]) = (l[j+1], l[j])
                swapped = True

            else:
                continue

        if swapped == False:
            break

            

print("Sorted array is:")
l = [5, 64, 89, 1, 6, 100, 74, 2]

bubble(l)
for i in range(len(l)):
    print("%d" % l[i], end=" ")

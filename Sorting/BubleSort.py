def bubleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print

if __name__ == '__main__':
    arr = [5,1,6,2,4,3]
    printList(arr)

    print("\nSorted Array : ")
    bubleSort(arr)
    printList(arr)
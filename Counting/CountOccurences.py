def countOccurences(test_str, charac):
    count = 0

    for i in test_str:
        if i == charac:
            count += 1

    print("\nThe total number of occurences of the character : " + str(charac) + " in the string : " + str(
        test_str) + " is :: " + str(count))


if __name__ == '__main__':
    test_str = 'akshaytiwari'

    search = input("Enter the character to search : ")
    countOccurences(test_str, search)

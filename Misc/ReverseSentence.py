def rev_sentence(sentence):

    # split the sentence based on the delimiter
    words = sentence.split(' ')

    # then reverse the split string list and join using the same delimiter
    reverse_sentence = ' '.join(reversed(words))

    # return the joined string
    return reverse_sentence

if __name__ == "__main__":
    input = 'coding is fun'
    print (rev_sentence(input))
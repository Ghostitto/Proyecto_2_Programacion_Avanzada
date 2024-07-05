# returns True if the word can be segmented into parts such
# that each part is contained in dictionary
def wordBreak(word):
   
    global dictionary

    size = len(word)

    # base case
    if (size == 0):
        return True

    # else check for all words
    for i in range(1,size + 1):
        # Now we will first divide the word into two parts ,
        # the prefix will have a length of i and check if it is
        # present in dictionary ,if yes then we will check for
        # suffix of length size-i recursively. if both prefix and
        # suffix are present the word is found in dictionary.

        if (word[0:i] in dictionary and wordBreak(word[i: size])):
            return True

    # if all cases failed then return False
    return False
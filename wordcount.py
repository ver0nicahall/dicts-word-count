import sys 

"""Count words in file."""

def count_words(filename):
    #input: text, output: dictionary {'word': number}
    """Returns a dictionary with counted words."""

    #initialize empty dictionary 
    word_count = {}

    #open file
    text_file = open(filename)

    #use for loop to iterate over text file
    for line in text_file:
        #strip whitespace and split by word
        words = line.strip().split(" ")
    
    #normalize text

        ### METHOD 2

        for word in words:
            #strip of punctuation
            punc = [',', '?', '']
            #if last character of word is punctuation
            if word[-1] in punc:
                #remove last character
                word = word[:-1]
            #remove case
            word = word.lower()
            word_count[word] = word_count.get(word,0) + 1

    ### method that doesn't use get
    # #iterate over list of words to count words
    # for word in list_of_words:
    #     #if word exists as a key in dictionary
    #     if word in word_count:
    #         #add 1 to value
    #         word_count[word] += 1
    #     #else create a key and set value to 1
    #     else:
    #         word_count[word] = 1

    #return dictionary of words
    return word_count

print(count_words("test.txt"))
def target_solver(centre_letter, outer_letters, dictionary='all_english_words.txt'):
    """
    finds a solutions to the target puzzle:
        Find words of four letters or more. 
        Every word must include the centre letter and each letter is used once only. 
        Find at least one nine-letter word. No colloquial or foreign words, 
        nouns, apostrophes or hyphens. 
        No verbs or plural words ending in "s". Solution list is not exhaustive.
    example:
        https://www.smh.com.au/national/target-time-and-superquiz-tuesday-may-11-20210510-p57qmb.html
    ----
    input:
        `centre_letter`: str
            the center letter of the puzzle which must be in each word
        `outer_letters`: str
            a string of size 8, which are other letters that can be used to make up a word
        `dictionary` : list containing str
            a list of words that will be checked for the target contraints
    returns: list of str
        a list where of words in `dictionary` that satify the target puzzle contraints.
    """

    all_letters = centre_letter + outer_letters

    # stores words that are valid for the target
    valid_words = []

    for word in dictionary:
        # words must have lengh greater than 4, and contain the target letter
        if len(word) >= 4 and centre_letter in word:
            # finds words which be made using only the provided letters
            include_word = True
            for letter in word:
                if word.count(letter) > all_letters.count(letter):
                    include_word = False
                    break
            if include_word:
                valid_words.append(word)
    # valid words is the solution to the puzzle
    return valid_words



def target(centre_letter, outer_letters, dictionary='all_english_words.txt'):
    """ 
    Prints a formatted solution for target to terminal 
    
    input:
        `centre_letter`: str
            the center letter of the puzzle which must be in each word
        `outer_letters`: str
            a string of size 8, which are other letters that can be used to make up a word
        `dictionary` : list containing str
            a list of words that will be checked for the target contraints
    returns: None
        prints to std out
    
    """

    # open dictionary, where each line is the txt file is an english word
    # all_english_words.txt contains all words in english language
    f = open("all_english_words.txt")
    # make a list where each element is an english word
    all_english_words= f.read().split('\n')
    f.close()

    # find all words that satify the target puzzle
    valid_words = target_solver(centre_letter, outer_letters, all_english_words)

    # print the result
    print()
    print("Total words found:", len(valid_words))
    print("All valid words:")
    for word in valid_words:
        print('\t', word)
    print("7 letter words:")
    for word in valid_words:
        if len(word) == 7:
            print('\t', word)


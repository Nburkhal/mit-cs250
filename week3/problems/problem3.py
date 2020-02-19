import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    
    available_letters = list(filter(lambda ch: ch not in lettersGuessed,
                                    all_letters))
    
    return ''.join(available_letters)
    
    


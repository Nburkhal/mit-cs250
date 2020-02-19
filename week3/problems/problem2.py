def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord = secretWord[:]
    guessedWord = ''

    for i in secretWord:
      if i in lettersGuessed:
        guessedWord += i
      else:
        guessedWord += '_'

    return guessedWord


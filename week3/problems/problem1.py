correct_guesses = []
    for i in secretWord:
      if i not in lettersGuessed:
        correct_guesses.append(False)
      else:
        correct_guesses.append(True)

    if False not in correct_guesses:
      return True
    else:
      return False

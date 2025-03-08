def check_word(word, available, required):
    """Check whether a word is acceptable.

       >>> check_word('color', 'ACDLORT', 'R')
       True
       >>> check_word('ratatat', 'ACDLORT', 'R')
       True
       >>> check_word('rat', 'ACDLORT', 'R')
       False
       >>> check_word('told', 'ACDLORT', 'R')
       False
       >>> check_word('bee', 'ACDLORT', 'R')
       False
       """
    word = word.lower()
    available = word.lower()
    required = required.lower()

    #rule #1 # word cant be smaller than 4 letters long
    if len(word) < 4:
        return False
    #rule #2 must have the required letter
    if required not in words:
        return False
    #rule #3 only letters from available
    for letter in word:
        if letter not in available:
            return False
    return True # if all rules are followed it will return True

# Run doctests (optional)
import doctest
doctest.testmod()
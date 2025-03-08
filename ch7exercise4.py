def uses_all(word, required):
    """Checks whether a word uses all required letters.

       >>> uses_all('banana', 'ban')
       True
       >>> uses_all('apple', 'api')
       False
       >>> uses_all('cherry', 'che')
       True
       >>> uses_all('orange', 'z')
       False
       """

    for letter in required: #this one takes letters in required, and if not in word is false
        if letter not in word:
            return False
    return True

#run doctest
import doctest
doctest.testmod()
        i
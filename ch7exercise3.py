def uses_only(word, available):
    """ checks whether a word uses only the available letters

    >>> uses_only('banana', 'ban')
    True
    >>>uses_only('apple', 'apl')
    False
     >>> uses_only('hello', 'helo')
    True
    >>> uses_only('world', 'worl')
    Falsed
    """
    for letter in word:
        if letter not in available: #if the letter is not in available it returns false
            return False
    return True
# Run doctests
import doctest
doctest.testmod()

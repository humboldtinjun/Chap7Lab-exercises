def uses_none(word, forbidden):
    """Checks whether a word is in forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('cherry', 'cr')
    False
    >>> uses_none('grape', 'xyz')
    True
    """
    for letter in word:  # loops through each letter in the word
        if letter in forbidden:  # check if the letter is in forbidden
            return False  #  return False immediately
    return True  #  if no forbidden letters were found return True


# doctests
import doctest

doctest.testmod()

# test cases 
print(uses_none("banana", "xyz"))  # Expected: True
print(uses_none("apple", "efg"))  # Expected: False
print(uses_none("grape", "xyz"))  # Expected: True
print(uses_none("cherry", "cr"))  # Expected: False


#ask VA whats wrong with uses_any function.
#incorrect code
def uses_any_incorrect(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else: # should be indented outside of the for loop
            return False  # INCORRECT!
### this is wrong because if you put the return false inside the for loop, then if the first
### letter is false, it wont check the rest of the word, placing it outside of the loop lets
### it check all the letters first before going to the next step in the function and returning false

#what it should look like
def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True  # Correctly returns if any letter matches
    return False  # Only return False if no match is found

def word_score(word, available):
    word = word.lower()
    available = available.lower()
    score = 0 # have to initialize it

    if len(word) == 4:
        score = score +1 # 4 letter words get 1 point

    if len(word) > 4:
        score = len(word) # add a point for every letter

    if all(letter in word for letter in set(available):
        score = score + 7

    return score

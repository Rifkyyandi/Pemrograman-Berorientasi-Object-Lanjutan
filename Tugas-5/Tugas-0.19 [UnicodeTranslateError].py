string = "Héllò"
table = str.maketrans({'é': 'e'})
new_string = string.translate(table) # UnicodeTranslateError: 'ascii' codec can't encode character '\xe9' in position 1: ordinal not in range(128)

with open('input.txt', 'x') as file:
    file.write(f"Beautiful is better than ugly. \nExplicit is better than implicit. \n"
               f"Simple is better than complex. \nComplex is better than complicated.")

with open('input.txt', 'r') as file:
    content = file.readlines()
    count_lines = 0
    count_words = 0
    count_letters = 0
    for lines in content:
        count_lines += 1
    for lines in content:
        a = lines.split(' ')
        a = [item for item in a if item != '\n']
        word = []
        for item in a:
            cleaned_item = item.replace('.', '')
            word.append(cleaned_item)
        count_words += len(word)
        for words in word:
            letters = list(words)
            count_letters += len(letters)
    print(f"Input file contains:\n{count_letters} letters\n{count_words} words\n{count_lines} lines")



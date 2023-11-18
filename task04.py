with open("banned words.txt", 'x') as file:
    file.write("hello email python the exam wor is")
with open('banned words.txt', 'r') as file:
    banned_words = file.read().split()


def censor(sentence, banwords):
    words = sentence.split()
    censored_words = list()
    for word in words:
        lowcase_word = word.lower()
        for banned_word in banwords:
            if lowcase_word.find(banned_word) >= 0:
                censored_word = lowcase_word.replace(banned_word, '*' * len(banned_word))
                censored_words.append(censored_word)
                break
        else:
            censored_words.append(word)
    censored_sentence = ' '.join(censored_words)
    return censored_sentence


sentence = "Hello, world ! Python IS the programming language of thE future. My EMAIL is .... PYTHON is awesome!!!!"
print(censor(sentence, banned_words))

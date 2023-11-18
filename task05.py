with open("осуждаем.txt", 'w') as file:
    file.write("черника помидоры")
with open('осуждаем.txt', 'r') as file:
    banned_words = file.read().split()


def censor(sentence, banwords):
    words = sentence.split()
    censored_words = list()
    for word in words:
        lowcase_word = word.lower()
        for banned_word in banwords:
            if lowcase_word.find(banned_word) >= 0:
                censored_word = lowcase_word.replace(banned_word, 'бан')
                censored_words.append(censored_word)
                break
        else:
            censored_words.append(word)
    censored_sentence = ' '.join(censored_words)
    return censored_sentence


sentence = "Сладкая черника и спелые помидоры - отличный выбор для здорового утреннего завтрака."
with open("одобряем.txt", 'x') as file:
    file.write(censor(sentence, banned_words))

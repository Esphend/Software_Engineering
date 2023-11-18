with open('funcstatecorrect.txt', encoding='utf-8') as file:
    content = file.read().split()
    words_total = 0
    word_count = {}
    for words in content:
        words_total += 1
    for word in content:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_freq_word = max(word_count, key=word_count.get)
print(f"Количество слов в статье: {words_total}\nСамое часто встречающееся слово: {most_freq_word}")
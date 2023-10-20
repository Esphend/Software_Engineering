string = input('Введите предложение на английском: ').lower()
count = 0
for letter in string:
    if letter == 'a' or letter == 'i' or letter == 'e' or letter == 'o' or letter == 'u':
        count += 1
xstring = string.replace("ugly", "beauty")
print(string)
print(f"Длина предложения = {len(string)}.")
print(f"Количество гласных (a,i,e,o,u) в тексте = {count}")
print(f"Отредактированная фраза: {xstring}")
print(f"Предложение начинается с артикля The - {xstring.startswith('the')}")
print(f"Предложение заканчивается на end - {xstring.endswith('end')}")
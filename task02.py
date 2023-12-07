def presence(file_name):
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            data = f.read()
            if not data:
                raise Exception("Файл пустой!")
            print(data)

    except Exception as e:
        print(e)

presence('blank.txt')
presence('filled.txt')
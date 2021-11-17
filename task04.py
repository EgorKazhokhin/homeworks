for filename in os.listdir('folder'):
    filepath = os.path.join('folder', filename)
    with open(filepath, mode='r') as f:
        content = f.read()
        print(content)  # распечатка всех файлов в каталоге


import requests

response = requests.get("https://epam.com")
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)  # скачать содержимое сайта и сохранить в файл



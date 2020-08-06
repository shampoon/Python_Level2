import hashlib

cash = {}
salt = '*#&$'
while True:
    url_name = input('Для выхода наберите "exit". Введите URL-адрес: ')
    if url_name == 'exit':
        print('До встречи!')
        break
    url_hash = hashlib.sha256((salt + url_name).encode('utf-8'))
    if cash.get(url_hash.hexdigest()) is None:
        cash[url_hash.hexdigest()] = url_name
    else:
        print('URL уже в кэше')
"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


class URLHash:
    salt = '*#&$'
    cash = {}

    def check_url(self, url):
        url_hash = hashlib.sha256((self.salt + url).encode('utf-8'))
        return (self.cash.get(url_hash.hexdigest()) is not None), url_hash

    def add_url(self, url):
        url_in_hash, url_hash = self.check_url(url)
        if url_in_hash:
            print('URL уже присутствует в хэше')
        else:
            print('Добавляем URL...')
            self.cash[url_hash.hexdigest()] = url


url_hash = URLHash()
while input('Хотите ввести новую ссылку? y/n ') == 'y':
    url_hash.add_url(input('Введите ссылку: '))
print('До скорых встречь!')

"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
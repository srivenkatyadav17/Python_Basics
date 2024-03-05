book = {'tom': {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': '89139942'
}, 'bob': {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': '57293472'
}}

import json

s = json.dumps(book)
with open('C://Users//srive//PycharmProjects//book.txt', 'w') as f:
    f.write(s)

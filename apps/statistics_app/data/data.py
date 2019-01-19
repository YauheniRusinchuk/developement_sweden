import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


path = os.path.join(BASE_DIR, 'data', 'data.txt')


def create():
    with open(path, 'w') as file:
        data = {}
        data['Profile'] = []
        json.dump(data, file)


def write_new_person(pk,username):
    with open(path, 'r') as file_r:
        data = json.load(file_r)

        with open(path, 'w') as file_w:
            data['Profile'].append({
                'id': pk,
                'username': username,
                'counts-note': 0,
            })

            json.dump(data, file_w)

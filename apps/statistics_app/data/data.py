import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


path = os.path.join(BASE_DIR, 'data', 'data.json')


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


def update_count_note(pk):
    with open(path, 'r') as file:
        data = json.load(file)

        with open(path, 'w') as file_w:
            for profile in data['Profile']:
                if profile['id'] == pk:
                    profile['counts-note'] = profile['counts-note'] + 1
            json.dump(data, file_w)



def read_statistics(pk):
    with open(path, 'r') as file:
        data = json.load(file)

        for profile in data['Profile']:
            if profile['id'] == pk:
                return profile

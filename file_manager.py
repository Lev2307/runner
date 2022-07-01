import pickle
import os
from settings import BASE_DIR

class FileManager:
    def check_datadir_exists_decorator(func):
        def wrapper(self, data, *args, **kwargs):
            if not os.path.exists(f'{BASE_DIR}\data'):
                os.mkdir('data')
            return func(self, data)
        return wrapper

    @check_datadir_exists_decorator
    def load_data(self, name):
        with open(f'{BASE_DIR}\data\{name}', 'rb') as f:
            data = pickle.load(f)
        return data

    @check_datadir_exists_decorator
    def save_data(self, data):
        new_data = data
        level_number = new_data['level']
        with open(f'{BASE_DIR}\data\level_{level_number}', 'wb') as f:
            pickle.dump(data, f)


test_data = {
    'level': 1,
    'obstacles': {
        'easy': 10,
        'medium': 5,
        'complex': 0,
    },
    'word': 'orange',
    'speed': 1,
}
f = FileManager()

f.save_data(test_data)

data = f.load_data('level_1')
print(data)
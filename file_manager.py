import pickle

class FileManager:
    def load_data(self, name):
        with open(f'{name}.bin', 'rb') as f:
            p = pickle.loads(f)
        return p
    
    def save_data(self, data):
        new_data = data
        level_int = new_data['level']
        with open(f'level_{level_int}.bin', 'wb') as f:
            pickle.dumps(f)

test_data = {
    'level': 1,
    'obstacles': {
        'easy': 30,
        'medium': 15,
        'hard': 5
    },
    'word': 'orange',
}
f = FileManager()

f.save_data(test_data)

f.load_data('level_1')
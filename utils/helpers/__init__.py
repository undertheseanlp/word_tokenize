import dill as pickle
import io


def save_data(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f, protocol=1)


def load_data(path):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model


def read(fname):
    with io.open(fname, 'r', encoding='utf-8') as fin:
        text = fin.read()
    return text


def flat_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

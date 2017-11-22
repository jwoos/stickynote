import functools
import hashlib
import random


def hash(data, length=0):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    sha256.update(str(random.randint(1000000000)))

    digest = sha256.hexdigest()[:]

    length = min(length, len(digest)) or len(digest)

    return digest[:length]

def compose(*functions):
    def _compose(g, f):
        return lambda *args, **kwargs: f(g(*args, **kwargs))

    return functools.reduce(_compose, functions)

def random_string_generator(length=8, count=10):
    source = string.ascii_letters + string.digits
    get_random_string = lambda l: ''.join(random.choice(source) for _ in range(l))
    used = set()
    current = 0

    while current < count:
        x = get_random_string(length)
        while x in used:
            x = get_random_string(length)

        used.add(x)

        yield x
        current += 1

    def dict_encode(schema, data):
        raw_data = {}

        for k, constructor in schema.items():
            _, deserializer = constructor

            if deserializer:
                raw_data[k.encode()] = deserializer(data[k])
            else:
                raw_data[k.encode()] = data[k]

        return raw_data

    def dict_decode(schema, raw_data):
        data = {}

        for k, constructor in schema.items():
            serializer, _ = constructor

            if serializer is not None:
                data[k.decode()] = serializer(raw_data[k])
            else:
                data[k.decode()] = raw_data[k]

        return data

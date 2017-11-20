import hashlib


def hash(title, message, length=0):
    sha256 = hashlib.sha256()
    sha256.update(title.encode())
    sha256.update(message.encode())

    digest = sha256.hexdigest()[:]

    length = min(length, len(digest)) or len(digest)

    return digest[:length]

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

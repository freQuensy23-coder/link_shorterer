import random, string


def generate_rand_hash(hash_len = 12):
    """Generates random hash to use it in links"""
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                   for _ in range(hash_len))

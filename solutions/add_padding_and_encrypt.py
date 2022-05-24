def add_padding_and_encrypt(username):
    if len(username) < 4:
        username += "X" * (4-len(username))
    return c6.encrypt(username)

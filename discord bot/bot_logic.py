from random import choice, randint
import string

chars = string.ascii_letters + string.digits + string.punctuation

def gen_pass(pass_length):
    pw = "".join(choice(chars) for _ in range(pass_length))
    return pw

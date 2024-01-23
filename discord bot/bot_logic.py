from random import choice, randint
import string

chars = string.ascii_letters + string.digits + string.punctuation

def gen_pass(pass_length):
    pw = "".join(choice(chars) for _ in range(pass_length))
    return pw

def flip_a_coin():
    if randint(0,1):
        return "heads"
    else:
        return "tails"
    
emoji_dict = [
    ":wave:",
    ":smile:",
    ":+1:",
    ":skull:",
    ":sunglasses:",
    ":billed_cap:",
    ":partying_face:",
    ":thinking:",
    ":eyes:",
    ":relieved:",
    ":joy:",
    ":flushed:",
    ":sob:",
    ":cry:",
    ":clown:",
    ":heart:",
    ":smiley:",
    ":fire:"
]

def random_emoji():
    return choice(emoji_dict)

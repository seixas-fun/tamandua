import random

def get_random_flag(category):
    # carregar lista de arquivos
    flags = load_flags(category)
    return random.choice(flags)

def generate_multiple_choice(correct, category):
    flags = load_flags(category)
    options = random.sample(flags, 3)
    options.append(correct)
    random.shuffle(options)
    return options
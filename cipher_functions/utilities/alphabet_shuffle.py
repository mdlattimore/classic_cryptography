import string, secrets

def shuffle():
    a = [char for char in string.ascii_uppercase]
    new = []
    for lett in range(len(a)):
        next = secrets.choice(a)
        new.append(next)
        a.remove(next)
    return "".join(new)


if __name__ == '__main__':
    shuff_list = shuffle()
    shuff_alpha = "".join(shuff_list)
    print(shuff_alpha)
    

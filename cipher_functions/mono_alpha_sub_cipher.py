from alphabet_shuffle import shuffle
import string

def shuffle_encrypt(msg):
    alphabet = string.ascii_uppercase
    key = shuffle()
    letter_map = dict(zip(alphabet, key))
    msg_list = [char for char in msg.upper()]
    enc_list = []
    for letter in (msg_list):
        if letter in alphabet:
            enc_list.append(letter_map[letter])
        else:
            enc_list.append(letter)
    enc_msg = "".join(enc_list)
    return (enc_msg, letter_map)
        

if __name__ == '__main__':
    msg = input("Enter message:")
    result = shuffle_encrypt(msg)
    enc_msg = result[0]
    key = result[1] 
    print(enc_msg)
    for k, v in key.items():
        print(f"{k}: {v}")


        
    

if __name__ == '__main__':
    shuffle_encrypt("msg")
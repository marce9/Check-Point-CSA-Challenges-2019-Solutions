import itertools
import string
N1 = 256


def KSA(key):
    key_length = len(key)
    # create the array "S"
    S = range(N1)  # [0,1,2, ... , 255]
    j = 0
    for i in range(N1):
        j = (j + S[i] + key[i % key_length]) % N1
        S[i], S[j] = S[j], S[i]  # swap values

    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % N1
        j = (j + S[i]) % N1

        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % N1]
        yield K

def get_keystream(key):
    S = KSA(key)
    return PRGA(S)

def encrypt(key, plaintext):
    keystream = get_keystream(key)

    res = []
    for c in plaintext:
        # val = ("%02X" % (ord(c) ^ next(keystream)))  # XOR and taking hex
        val = ("%02X" % (c ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return [''.join(res), res]

def encrypt_cypher(key, ciphertext):
    keystream = get_keystream(key)

    res = []
    for c in ciphertext:
        val = ("%02X" % (int(c, 16) ^ next(keystream)))  # XOR and taking hex
        res.append(val)
    return ''.join(res)

def decrypt(key, cipher):
    # ciphertext = ciphertext.decode('hex')
    # print 'ciphertext to func:', ciphertext  # optional, to see
    res = encrypt_cypher(key, cipher)
    return res.decode('hex')


def main():
    include_falling = [[9],  # 0 - debug
              [23],  # 1 - debug
              [6, 3, 4, 21, 18, 10, 11, 12, 1],  # 2 - debug
              [24, 13, 17],  # 3
              [18, 15, 17, 20, 2, 4, 11, 9, 21],  # 4
              [24, 1, 18, 6, 15, 10],  # 5
              [3],  # 6
              [1, 3],  # 7
              [5, 11],  # 8
              [8, 1],  # 9
              [6, 24, 23],  # 10
              [6, 24, 23, 3],  # 11
              [3],  # 12
              [20, 5],  # 12b/13 - 20 by code, 5 by internet
              [3]]  # potions level (15) room - 3 (debug)

    lists2 = [[9], # 0 - debug
             [23], # 1 - debug
             [6], # 2 - debug
             [24], # 3
             [18, 7], # 4
             [24], # 5
             [3], # 6
             [1, 3], # 7
             [5, 11], # 8
             [8, 1], # 9
             [6, 24, 23], # 10
             [6, 24, 23, 3], # 11
             [3], # 12
             [20, 5], # 12b/13 - 20 by code, 5 by internet
             [3]] # potions level (15) room - 3 (debug)

    lists_plus_fall = [[9],  # 0 - debug
              [23],  # 1 - debug
              [6],  # 2 - debug
              [24],  # 3
              [18, 7],  # 4
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],  # 5
              [3],  # 6
              [1, 3],  # 7
              [5, 11],  # 8
              [8, 1, 3],  # 9
              [6, 24, 23],  # 10
              [23, 13, 21, 11, 17],  # 11
              [13, 3, 2],  # 12
              [20],  # 12b/13 - 20 by code, 5 by internet
              [3]]  # potions level (15) room - 3 (debug)


    lists3 = [[9], # 0 - debug
             [23], # 1 - debug
             [6], # 2 - debug
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 3
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 4
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 5
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 6
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 7
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 8
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 9
              [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], # 10
             [23], # 11
             [3], # 12
             [20], # 12b/13 - 20 by code, 5 by internet
             [3]] # potions level (15) room - 3 (debug)


    lists4 = [[9],  # 0 - debug
              [23],  # 1 - debug
              [6],  # 2 - debug
              [1, 24],  # 3
              [18, 7],  # 4
              [24],  # 5
              [3],  # 6
              [1, 3],  # 7
              [5, 11],  # 8
              [8, 1],  # 9
              [6, 24, 23],  # 10
              [6, 24, 23, 3],  # 11
              [3],  # 12
              [20, 5],  # 12b/13 - 20 by code, 5 by internet
              [3]]  # potions level (15) room - 3 (debug)


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],


    for key in itertools.product(*lists_plus_fall):
        key = list(key)
        # print key
        plaintext = [214, 85, 173, 9, 13, 217, 126, 133, 241, 98, 37, 11, 50, 52, 8, 18, 230, 22, 122, 125, 160, 86, 8, 226,
                    17, 235, 234, 154, 238, 250, 210, 123, 171, 178, 43, 98, 237, 136, 68, 184, 17, 74, 113, 74, 138]

        # encrypt the plaintext, using key and RC4 algorithm
        [ciphertext, cipher_list] = encrypt(key, plaintext)
        # cipher_ord = map(ord, ciphertext.decode('hex'))

        # print str(key)
        # print ciphertext.decode('hex') + '\n'
        # print ciphertext.decode('hex')

        # # CSA{ (hex) = 43 53 41 7B
        # if decoded_cipher.decode('hex')[0] in 'C'\
        #         and decoded_cipher.decode('hex')[1] in 'S':
        #     print decoded_cipher + ' ' + decoded_cipher.decode('hex')

        # print str(key)
        # print ciphertext.decode('hex') + '\n'

        if all(c in string.printable for c in ciphertext.decode('hex')):
            print str(key)
            print ciphertext.decode('hex') + '\n'

        if 'CSA' in ciphertext.decode('hex'):
            print str(key)
            print ciphertext.decode('hex') + '\n'

        if 'CSA{' in ciphertext.decode('hex'):
            print str(key)
            print ciphertext.decode('hex') + '\n'


if __name__ == '__main__':
    main()
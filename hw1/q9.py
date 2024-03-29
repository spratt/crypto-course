# Decode the two ciphertexts from the Instructors Box below, 
# or the C1, C2 variables - which are the same
#
# We highly recommend that you run your decoding code in the 
# programming language of your choice outside of the 
# this environment, as this system does not provide enough 
# computational resources to successfully decode
#
# After decoding the two ciphertexts, 
# replace the plaintext1 and plaintext2 variables below
# with the decoded ciphertexts

# C1 and C2 are messages in english, 
# encoded using string_to_bits, with 7bit ASCII
# and then XOR'd with a secret key
#
# In pseudo-code:
# C1 = XOR(string_to_bits(plaintext1), secret_key)
# C2 = XOR(string_to_bits(plaintext2), secret_key)

C1 = "1010110010011110011111101110011001101100111010001111011101101011101000110010011000000101001110111010010111100100111101001010000011000001010001001001010000000010101001000011100100010011011011011011010111010011000101010111111110010011010111001001010101110001111101010000001011110100000000010010111001111010110000001101010010110101100010011111111011101101001011111001101111101111000100100001000111101111011011001011110011000100011111100001000101111000011101110101110010010100010111101111110011011011001101110111011101100110010100010001100011001010100110001000111100011011001000010101100001110011000000001110001011101111010100101110101000100100010111011000001111001110000011111111111110010111111000011011001010010011100011100001011001101110110001011101011101111110100001111011011000110001011111111101110110101101101001011110110010111101000111011001111"

C2 = "1011110110100110000001101000010111001000110010000110110001101001111101010000101000110100111010000010011001100100111001101010001001010001000011011001010100001100111011010011111100100101000001001001011001110010010100101011111010001110010010101111110001100010100001110000110001111111001000100001001010100011100100001101010101111000100001111101111110111001000101111111101011001010000100100000001011001001010000101001110101110100001111100001011101100100011000110111110001000100010111110110111010010010011101011111111001011011001010010110100100011001010110110001001000100011011001110111010010010010110100110100000111100001111101111010011000100100110011111011001010101000100000011111010010110111001100011100001111100100110010010001111010111011110110001000111101010110101001110111001110111010011111111010100111000100111001011000111101111101100111011001111"

#####
# CHANGE THESE VARIABLES

plaintext1 = "decoded message"
plaintext2 = "the other decoded message"

# END
#############

#############
# Below is some code that might be useful
#

BITS = ('0', '1')
ASCII_BITS = 7

def enquote(s):
    return '"' + s + '"'

def is_letter(c):
    o = ord(c)
    return ( o >= 65 and o <= 90 ) or ( o >= 97 and o <= 122 )

def is_digit(c):
    o = ord(c)
    return o >= 48 and o <= 57

def is_display(c):
    o = ord(c)
    return o >= 32 and o <= 126

def is_display_str(s):
    for c in s:
        if not is_display(c):
            return False
    return True

def display_bits(b):
    """ converts list of {0, 1}* to string """
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    """ converts a string of {'0','1'}* to a list of bits """
    return [0 if b == '0' else 1 for b in seq]

def XOR_bit(b1,b2):
    """ XORs a single bit with a single other bit """
    return 0 if b1 == b2 else 1

def XOR(bl1, bl2):
    """ returns the XOR of two bit lists """
    assert len(bl1) == len(bl2)
    return [XOR_bit(bl1[i],bl2[i]) for i in range(len(bl1))]

def pad_bits(bits, pad):
    """ pads seq with leading 0s up to length pad """
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """ converts an integer `n` to bit array """
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = n / 2
    return result

def string_to_bits(s):
    """ converts a string to a list of bits """
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_num(b):
    """ converts a list of bits to a single number """
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return value

def bits_to_char(b):
    """ converts a list of bits to a single char """
    return chr(bits_to_num(b))

def list_to_string(p):
    """ the hell does this do? """
    return ''.join(p)

def bits_to_string(b):
    """ converts a list of bits to the string of characters """
    return list_to_string([bits_to_char(b[i:i + ASCII_BITS]) 
                           for i in range(0, len(b), ASCII_BITS)])

def bits_to_nums(b):
    """ converts a list of bits to a list of numbers """
    return [bits_to_num(b[i:i + ASCII_BITS]) 
            for i in range(0, len(b), ASCII_BITS)]

def nums_to_string(lon):
    """ converts a list of numbers to a string """
    str = ""
    for i in range(0, len(lon)):
        str += chr(lon[i])
    return str
    
def add_word_to_bits(lob,word,pos):
    """ Adds the values of a given word to a list of bits """
    nums = bits_to_nums(lob)
    assert pos + len(word) <= len(nums)
    wnums = bits_to_nums(string_to_bits(word))
    return [nums[pos+i] + wnums[i] for i in range(0,len(word))]
    
def xor_word_to_bits(lob,word,pos):
    """ xors the bits of a given word with a list of bits """
    assert pos + len(word) <= len(lob)/7
    wbits = string_to_bits(word)
    return [XOR_bit(lob[pos*7+i],wbits[i]) for i in range(0,len(word)*7)]

def xor_word_bits_sequence_display(lob,word,display):
    """ xors the bits of a given word with a list of bits sequentially """
    pos = 0
    word = word.title() + ' '
    while pos + len(word) <= len(lob)/7:
        if pos == 1:
            word = ' ' + word.lower()
        if pos + len(word) == len(lob)/7:
            word = word[:len(word)-1] + '.'
        decode = bits_to_string(xor_word_to_bits(lob,word,pos))
        if display or is_display_str(decode):
            print "Position:", pos
            print "Word:", '"' + word + '"'
            print '"' + decode + '"'
            raw_input("Press any key to continue...")
        pos += 1

def xor_word_bits_sequence(lob,word):
    xor_word_bits_sequence_display(lob,word,False)

def decrypt(string,pos):
    print '->',enquote(bits_to_string(xor_word_to_bits(C1XORC2,string,pos)))

C1XORC2 = XOR(seq_to_bits(C1),seq_to_bits(C2))

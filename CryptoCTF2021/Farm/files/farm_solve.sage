import string, base64, math

def maptofarm(c):
	assert c in ALPHABET
	return F[ALPHABET.index(c)]

enc = '805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj'

ALPHABET = string.printable[:62] + '\\='

F = list(GF(64))

inv_F = {} 
index = 0                                                               
for i in F: 
    inv_F[i] = index 
    index+=1

inv_dict = {}
index = 0
for i in ALPHABET: 
     inv_dict[i] = index 
     index+=1

key_target = F[8]/maptofarm('Q') # Key used to compute value


res = ''                                                                  
for i in enc: 
    res += ALPHABET[inv_F[F[inv_dict[i]]/key_target]]

print(base64.b64decode(res))

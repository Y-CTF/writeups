#Write-up by  Grimlix & Grimlix
# Mac/Linux: pip3 install pycryptodome
# Windows: py -m pip install pycryptodome
import hashlib

import Crypto.Util.number as cun
from Crypto.Cipher import AES

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def flag():
    p = 6810447811852575014526351815145313582532890396094233411017184242379362913957152104043621525641876143780264309154808504992348019610268195737740949081211317
    g = 5
    print(f"p = {p}")
    print(f"g = {g}")

    A = 822085697150848843298997091776184435273976861693787075628751974260741594582396863345806538443623005065121172196860274197534588380991279550503983758155816
    b = 1
    B = pow(g, b, p)
    #shared_secret = pow(B, a, p)
    #print("keyPowShared", shared_secret)
    key = pow(A, b, p)
    print("keyPow", key)
    print("B", B)
    print("------------")

    key = hashlib.sha1(cun.long_to_bytes(key)).digest()[:16]
    print("keyhash", key)
    ciphertext = bytes.fromhex("8d69c846f5ae7299140ba9f1e597530907fb5cf963b8ff34a288ba4b213dd01990ec392a3c9366c62c4781c5bcbe20a9bac67fffa2be28c7d821d9d566dd1531")
    cipher = AES.new(key, AES.MODE_ECB)
    plain = cipher.decrypt(ciphertext)
    print(plain)
    print("flag", plain.decode('utf-8'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flag()


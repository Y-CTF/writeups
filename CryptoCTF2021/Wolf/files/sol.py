from pwn import xor
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long

passphrase = b'HungryTimberWolf'

enc = bytes.fromhex('85cb0a56016c5b28ee2f8309074ee88e6fe39ac12ac97a4669732d6d6f6e5e3f704b83b82191e09cc1bbca83ce185480a32ab5c770ebd92997b039d5d5fbb1b2471bf79e7e6fc5dfe7872305b153c35667e72912281703c3fd83592441232f63')
first_block = b'EPOCH:1627981541' # Might have to check for an interval a bit after but should not be a problem



ctr_enc = xor(first_block, enc[:16])
ctr_p2 = AES.new(passphrase, AES.MODE_ECB).decrypt(ctr_enc)
ctr = long_to_bytes(bytes_to_long(ctr_p2) - 1)
ctr = ctr.rstrip(b'\x00')

data = AES.new(passphrase, AES.MODE_GCM, nonce=ctr).decrypt(enc)
print(data)

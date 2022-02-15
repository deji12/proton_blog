# from pytube import YouTube
# link = input('link: ')
# print()
# yt = YouTube(link)
# print(yt.thumbnail_url)
from cryptography.fernet import Fernet
message = 'i like to code'.encode()
key = Fernet.generate_key()
fernet = Fernet(key)
enc = fernet.encrypt(message)
dec = fernet.decrypt(enc)
print(enc)
print(dec.decode())
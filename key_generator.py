from cryptography.fernet import Fernet
import os

def key_generator(encryption_key_filename):
  key = Fernet.generate_key()
  with open(encryption_key_filename, "wb") as file:
    file.write(key)
  return os.path.abspath(encryption_key_filename)
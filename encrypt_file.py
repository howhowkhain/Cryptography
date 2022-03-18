import errno
import sys
import os
from cryptography.fernet import Fernet
from key_generator import key_generator


def load_key(key_file):
  try:
    file = open(key_file, 'rb')

  except IOError as exc:

    if exc.errno == errno.ENOENT:
      user_answear = input(f"""There is no encryption key file with the name {os.path.basename(key_file)}.\nTo generate an encryption key file choose (Y/N): """).lower().strip()

      while user_answear.isalnum and user_answear != "y" and user_answear != "n":
        user_answear = input("""Incorect input. Choose (Y/N): """).lower().strip()

      if user_answear == "n":
        exit("No encryption key file was created. Exit script.")

      elif user_answear == "y":
        encryption_key_filename = input("Give a name for encryption key file: ").strip(" ")
        if encryption_key_filename == '':
          encryption_key_filename = 'key'
        key_file_path = key_generator(f"{encryption_key_filename}.key")
        print(f"Encryption key file was created at {os.path.abspath(key_file_path)}")
        file = open(key_file_path, 'rb')
        return file.read()
  else:
    return file.read()

def encrypt(file_to_encrypt, key_file="key.key"):
  encryption_key = load_key(key_file)
  f = Fernet(encryption_key)
  with open(file_to_encrypt, 'rb') as file:
    file_data = file.read()
  data_encrypted = f.encrypt(file_data)
  file_name, file_extension = os.path.splitext(file_to_encrypt)
  with open(f'{file_name}-ENCRYPTED{file_extension}', 'wb') as file:
    file.write(data_encrypted)

if len(sys.argv) not in [2, 3]:
  exit("""Improper number of arguments: at least one is required and not more than two are allowed:
  - file's pathname to be encrypted;
  - encryption key file's pathname required for encryption;
  """)

elif len(sys.argv) == 2:
  # script_pathname = sys.argv[0]
  # file_pathname = sys.argv[1]
  script_pathname, file_pathname = sys.argv
  encrypt(file_pathname)

elif len(sys.argv) == 3:
  # script_pathname = sys.argv[0]
  # file_pathname = sys.argv[1]
  # key_pathname = sys.argv[2]
  script_pathname, file_pathname, key_pathname = sys.argv
  encrypt(file_pathname, key_pathname)
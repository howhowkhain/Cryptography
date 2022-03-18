from cryptography.fernet import Fernet
import os
import sys
import errno

def load_key(key_file):
  try:
    file = open(key_file, 'rb')
  except IOError as exc:
    if exc.errno == errno.ENOENT:
      exit(f"""There is no decryption key file with the name {os.path.basename(key_file)}.\nTry another decyrption key file name as a second argument!""")
  else:
    return file.read()

def decrypt_file(file_to_decrypt, key_file="key.key"):
  decryption_key = load_key(key_file)
  f = Fernet(decryption_key)
  with open(file_to_decrypt, 'rb') as file:
    file_data = file.read()
    decrypted_data = f.decrypt(file_data)
    file_name, file_extension = os.path.splitext(file_to_decrypt)
  with open(f'{file_name.rstrip("-ENCRYPTED")}-DECRYPTED{file_extension}', 'wb') as file:
    file.write(decrypted_data)

if len(sys.argv) not in [2, 3]:
  exit("""Improper number of arguments: at least one is required and not more than two are allowed:
  - file's pathname to be decrypted;
  - decryption key file's pathname required for decryption (same encryption key used for file encryption);
  """)

elif len(sys.argv) == 2:
  # script_pathname = sys.argv[0]
  # file_pathname = sys.argv[1]
  script_pathname, file_pathname = sys.argv
  decrypt_file(file_pathname)

elif len(sys.argv) == 3:
  # script_pathname = sys.argv[0]
  # file_pathname = sys.argv[1]
  # key_pathname = sys.argv[2]
  script_pathname, file_pathname, key_pathname = sys.argv
  decrypt_file(file_pathname, key_pathname)
Encrypting and decrypting files using Fernet library

ATTENTION: Once a file is encrypted with a certain encryption key, it can be decrypted only using the same key. Otherwise all data will be lost.

================================================================================

ENCRYPTION:

- change directory to where the script is located

cd [script filepath]

The script can be run with:

One argument [file's path to be encrypted]:

- run encryption script without an encryption key argument will try to use the default encryption key file (key.key) from the script's directory and after will encrypt the file using this key file. If the key.key file doesn't exist it will ask to create one of any name. If no name provided it will create the default key.key file:

python encrypt_file.py [file to be encrypted path]

Two arguments [file's path to be encrypted] and [encryption key's path]:

- run encryption script with a encryption key file of your choice to encrypt the file:

python encrypt_file.py [file to be encrypted path] [encryption key file's path]

==================================================================================

DECRYPTION (use the same key used for encryption):

- change directory to where the script is located

cd [script filepath]

The script can be run with:

One argument [file's path to be decrypted]:

- run decryption script without specifying a decryption key file argument will use the default decryption key (key.key) if exist in the script's directory, and after will decrypt the file using this key file. If the file doesn't exist the script will be terminated.:

python decrypt_file.py [file's path to be decrypted]

Two arguments [file's path to be decrypted] and [decryption key file's path]:

- run decryption script with a decryption key file of your choice (same as the one used for encrypting) to decrypt the file:

python encrypt_file.py [file to be encrypted path] [encryption key's path]

import base64
import argparse

from cryptography.fernet import Fernet


def encrypt_file(filename, key):
    """
    Cifra el contenido del archivo dado usando la clave proporcionada.
    """
    with open(filename, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    with open(filename + ".encrypted", 'wb') as file:
        file.write(encrypted_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File encryptor")
    parser.add_argument("filename", help="Name of the file to encrypt.")
    parser.add_argument("-k", "--key", help="Key to use for encryption.")
    args = parser.parse_args()

    if not args.key:
        key = Fernet.generate_key()
        base64_key = base64.encodebytes(key).decode()
    else:
        try:
            key = args.key
            key = base64.decodebytes(key.encode())
            base64_key = args.key
        except Exception as e:
            print("Provided key is not valid.")
            exit(1)

    print(f"[!] Key: {base64_key}")
    print("[!] Encrypting file...")

    encrypt_file(args.filename, key)

    print(f"[*] File encrypted successfully: {args.filename}.encrypted")

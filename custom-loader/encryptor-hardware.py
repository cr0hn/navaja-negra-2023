import base64
import argparse
import os

import psutil
import hashlib

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_signature():
    # Datos del CPU
    cpu_info = {
        "physical": psutil.cpu_count(logical=False),
        "logical": psutil.cpu_count(logical=True),
        "freq": psutil.cpu_freq().current
    }

    # Datos de la memoria
    ram_info = {
        "total": psutil.virtual_memory().total,
        "swap": psutil.swap_memory().total,
    }

    # Información de las tarjetas de red
    macs = []
    for iface, addrs in psutil.net_if_addrs().items():
        # Get MAC address
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                macs.append(addr.address)

    # Juntar toda la información en una cadena
    signature = []

    # CPU
    signature.append(f"{cpu_info['physical']}")
    signature.append(f"{cpu_info['logical']}")
    signature.append(f"{cpu_info['freq']}")

    # RAM
    signature.append(f"{ram_info['total']}")
    signature.append(f"{ram_info['swap']}")

    # MACs
    signature.append(f"{''.join(macs)}")

    # Create a unique signature with SHA-512
    return hashlib.sha256(''.join(signature).encode()).digest()


def encrypt_file(filename, key):
    """
    Cifra el contenido del archivo dado usando la clave proporcionada.
    """
    with open(filename, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    with open(filename + ".encrypted-hardware", 'wb') as file:
        file.write(encrypted_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File encryptor")
    parser.add_argument("filename", help="Name of the file to encrypt.")
    args = parser.parse_args()

    password = generate_signature()
    # base64_key = base64.urlsafe_b64encode(key).decode()

    salt = os.urandom(16)  # Puedes guardar esta sal para derivar la misma clave en el futuro.

    # Derivamos una clave a partir de la contraseña usando PBKDF2 y SHA-256.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # key = kdf.derive(password)

    k = base64.urlsafe_b64encode(kdf.derive(password))

    # print(f"[!] Key: {base64_key}")
    print("[!] Encrypting file...")

    encrypt_file(args.filename, k)

    print(f"[*] File encrypted successfully: {args.filename}.encrypted")

if __name__ == "__main__":
    print(generate_signature())

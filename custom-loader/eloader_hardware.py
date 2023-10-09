import hashlib
import base64
import inspect

import psutil

from cryptography.fernet import Fernet


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
    signature = hashlib.sha512(''.join(signature).encode()).hexdigest()

    return signature


def decrypt_and_run(f: str):
    with open(f, 'rb') as file:
        content_file = file.read()

    try:
        key = base64.decodebytes(generate_signature())
    except Exception as e:

        if hasattr(key, 'decode'):
            key = key.decode()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(content_file)

    exec(decrypted_data.decode(), globals())

    local_ns = {}
    exec(decrypted_data.decode(), globals(), local_ns)

    # Ahora, accede al frame del caller
    caller_frame = inspect.currentframe().f_back

    # Inyecta las variables locales de decrypt_and_run en el espacio de nombres global del caller
    caller_frame.f_globals.update({k: v for k, v in local_ns.items() if k not in caller_frame.f_globals})


if __name__ == "__main__":
    print(generate_signature())

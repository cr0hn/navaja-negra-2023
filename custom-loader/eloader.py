import base64
import inspect

from cryptography.fernet import Fernet


def decrypt_and_run(f: str, key: str):
    with open(f, 'rb') as file:
        content_file = file.read()

    try:
        key = base64.decodebytes(key.encode())
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

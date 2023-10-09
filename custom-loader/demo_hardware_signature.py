from eloader_hardware import decrypt_and_run


def main():
    # Load encrypted file
    decrypt_and_run("secret_library.py.encrypted")

    # super_secret_algorithm()
    print("The answer to life, the universe and everything is: ")

    print(super_secret_algorithm())


if __name__ == '__main__':
    main()

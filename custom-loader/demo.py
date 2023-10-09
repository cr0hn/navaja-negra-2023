from eloader import decrypt_and_run


def main():
    # Load encrypted file
    decrypt_and_run("secret_library.py.encrypted", "UVktZE94cUotd3Nwdm5pMUMzcDR6NUMwek1QbFZoSm1NUmJnU3FzNnUwWT0=")

    # super_secret_algorithm()
    print("The answer to life, the universe and everything is: ")

    print(super_secret_algorithm())


if __name__ == '__main__':
    main()

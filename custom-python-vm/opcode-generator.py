import os
import re
import random
import argparse

REGEX_DEFINE = re.compile(r'(#define\s+\w+\s+)(\d+)')


def generate_random_opcode(existing: set):
    while 1:
        proposed = random.randint(0, 255)

        if proposed not in existing:
            return proposed

        existing.add(proposed)


def randomize_defines(input_file):
    used_values = set()

    for f in input_file:

        # Read the input file
        with open(f, 'r') as file:
            lines = file.readlines()

        # Procesar cada línea
        updated_lines = []
        for line in lines:
            # Buscar líneas que comienzan con '#define'
            if found := REGEX_DEFINE.match(line):
                # Reemplazar el valor numérico con un valor entero aleatorio nuevo
                new_value = generate_random_opcode(used_values)
                updated_line = f'{found.group(1)}{new_value}\n'

            else:
                # Dejar la línea sin cambios si no es una línea '#define'
                updated_line = line

            updated_lines.append(updated_line)

        # Escribir el archivo de salida
        f_name, f_ext = os.path.splitext(f)

        with open(f"{f_name}.shuffled.h", 'w') as file:
            file.writelines(updated_lines)


def main():
    parser = argparse.ArgumentParser(description='Randomize #define values in a .h file.')
    parser.add_argument('input_files', help='Path to the .h file to process.', nargs='+')

    args = parser.parse_args()

    randomize_defines(args.input_files)


if __name__ == '__main__':
    main()

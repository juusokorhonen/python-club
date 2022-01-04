import os


def main():
    files = os.listdir('.')
    print(",\n ".join(files))

    # Remove '.py' suffix
    new_files = [x.removesuffix('.py') for x in files]
    print(",\n ".join(new_files))

    # Remove '.' prefix
    new_files_2 = [x.removeprefix('.') for x in files]
    print(",\n ".join(new_files_2))

    # Not rstrip
    new_files_3 = [x.rstrip('.py') for x in files]
    print(",\n ".join(new_files_3))


if __name__ == "__main__":
    main()

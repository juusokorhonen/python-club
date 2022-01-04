
def main():
    x, y = 5, 6

    family = "smith john betty elisabeth barty"
    lastname, *firstnames = family.split()
    print(f"The {lastname.capitalize()}s:")
    for firstname in firstnames:
        print("\t" + firstname.capitalize())


if __name__ == "__main__":
    main()


def main():
    team_members = {
        input('name? '): input('position? ') for _ in range(3)
    }
    print(team_members)


if __name__ == "__main__":
    main()

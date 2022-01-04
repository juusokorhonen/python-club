import os


def main():
    # Lists
    a = [1, 2, 3]
    b = [3, 4]
    print(a+b)

    # Sets
    c = {1, 2, 3}
    d = {3, 4}
    print(c | d)

    # Dicts (new in 3.9)
    e = {'foo': 1, 'bar': 2, 'baz': 3}
    f = {'baz': 4, 'fux': 5}
    print(e | f)
    print(f | e)

    # Assigment, replaces e.update(f)
    e |= f
    print(e)

    # Example
    my_env_vars = {
        'MY_VAR': "foobar",
        'USER': "temp user"
    }
    my_env_vars |= os.environ
    print(my_env_vars)


if __name__ == "__main__":
    main()

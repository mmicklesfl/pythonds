def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    try:
        with open(filename, 'r') as file:
            for line in file:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


read_file_list("dogs")

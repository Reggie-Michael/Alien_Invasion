import os


def get_file_path(filename, folder="images"):
    """This returns an image path

    Args:
        filename (str): name of the file
    """
    return os.path.join(folder, filename)


def get_value_by_level(level):
    """Return a value based on the level range.

    Special handling for multiples of 10:
    - 10 -> return 0
    - 20 -> return 1
    - 30 -> return 2
    - 40 -> return 0
    - 50 -> return 1
    - and so on...

    Other numbers:
    - 1-3 -> return 0
    - 4-6 -> return 1
    - 7-9 -> return 2
    - 11-13 -> return 0
    - and so on...
    """
    if level % 10 == 0:
        # Multiples of 10 follow a different pattern (0, 1, 2, ...)
        return (level // 10 - 1) % 3

    mod_value = (level - 1) % 9
    if 0 <= mod_value <= 2:
        return 0
    elif 3 <= mod_value <= 5:
        return 1
    elif 6 <= mod_value <= 8:
        return 2

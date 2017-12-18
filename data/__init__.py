import os


def get_current_dir(current_file):
    return os.path.dirname(os.path.abspath(current_file))


DATA_DIR = get_current_dir(__file__)

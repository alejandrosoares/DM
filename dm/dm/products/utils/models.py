from django.conf import settings
from PIL import Image


def get_file_name(path):
    """Get file name of path
    @param: str
    @return: str
    """
    index = path.rfind('/')

    return path[index + 1:]


def get_extension(file):
    """Get extension of file name
    @param: str
    @return: str
    """

    dot_index = file.rfind(".", 1)

    return file[dot_index:]


def replace_extension_to_webp(path):
    """ Replace extension to webp

    @param: str
    @return: str
    """

    extension = get_extension(path)

    return path.replace(extension, '.webp')


def get_small_filename(filename):
    """ Build small filename
    Example: 2.png -> 2_small.png
    @param: str
    @return: str
    """

    dot_index = filename.rfind('.')

    return filename[:dot_index] + '_small' + filename[dot_index:]


def get_path(path):
    """ Get path

    @param: str
    @return: str
    """
    slash_index = path.rfind('/', 1)

    return path[:slash_index]

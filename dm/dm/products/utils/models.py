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

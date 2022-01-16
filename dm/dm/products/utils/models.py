def get_file_name(path):

    index = path.rfind('/')

    return path[index + 1:]


def get_extension(file):
    dot_index = file.rfind(".", 1)
    return file[dot_index:]

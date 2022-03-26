def get_filename(name):
    complete = name.split(".")
    if len(complete) == 2:
        return complete[0]
    complete.pop(-1)
    return ".".join(complete)

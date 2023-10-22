from functools import partial


def deprecated(f=None, *, since=None, will_be_removed=None):
    if f is None:
        return partial(deprecated, since=since,
                       will_be_removed=will_be_removed)
    warning = f"Warning: function {f.__name__} is deprecated"
    warning += f" since version {since}. " if since else ". "
    if will_be_removed:
        warning += f"It will be removed in version {will_be_removed}"
    else:
        warning += "It will be removed in future versions"

    def inner(*args, **kwargs):
        print(warning)
        return f(*args, **kwargs)
    return inner


@deprecated(since=14.1)
def lol():
    print("lol")


lol()

import functools


# it seems like the outer function takes the function you are decorating, and the other args get passed to the inner function, which, yeah, makes sense
def do_twice(fn):
    # uses functools.update_wrapper() to update special attributes like __name__ and __doc__ that are used in the introspection

    @functools.wraps(fn)
    # I assume that args is for positional, and kwargs is for keyword args
    # Now accepts any number of those args and passes them onto the function that it decorates
    def wrapper_do_twice(*args, **kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)

    return wrapper_do_twice

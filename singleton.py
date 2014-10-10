# -*- coding: utf-8 -*-
"""A non-thread-safe helper class to ease implementing singletons.

This should be used as a decorator -- not a metaclass -- to the
class that should be a singleton.

The decorated class can define one `__init__` function that
takes only the `self` argument. Other than that, there are
no restrictions that apply to the decorated class.

To get the singleton instance, use the `Instance` method. Trying
to use `__call__` will result in a `TypeError` being raised.

Limitations: The decorated class cannot be inherited from.

"""

all = ("Singleton")


class Singleton:

    """Example Usage.

    @Singleton
    class Foo:
        def __init__(self):
            print('Foo created')
            self.hi = "No"

    #import singleton
    from singleton import Foo
    f = Foo.Instance()  # Good. Being explicit is in line with the Python Zen
    g = Foo.Instance()  # Returns already created instance

    print(f is g)  # True
    """

    def __init__(self, decorated):
        """Create the singleton."""
        self._decorated = decorated

    def Instance(self):
        """Return the singleton instance.

        Upon first call, it creates a new instance of the decorated class
            and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        """Raise an error if `Instance()` is not used."""
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        """Check for an instance."""
        return isinstance(inst, self._decorated)

class Borg:
    """Borg class making class attribute global"""
    _shared_state = {}  # Attribute dictionary

    def __init__(self):
        # Make it an attribute dictionary
        self.__dict__ = self._shared_state


class Singleton(Borg):  # Inherits from the Borg class
    """ This class now shares all its attributes among its various instances"""
    # This essentially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


if __name__ == '__main__':
    # Let's create a singleton object and add our first acronym
    x = Singleton(HTTP="Hyper Text Transfer Protocol")

    # Print the object
    print(x)

    # Let's create another singleton object and if it refers to the same attributes dictionary by adding another acronym
    y = Singleton(SNMP="Simple Network Management Protocol")

    print(y)


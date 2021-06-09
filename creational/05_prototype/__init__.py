import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)

        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


if __name__ == '__main__':
    c = Car()
    prototype = Prototype()
    prototype.register_object("skylar", c)

    # Cloning the object
    c1 = prototype.clone("skylar")

    print(c1)

    # Cloning the object with attributes
    c2 = prototype.clone("skylar", options="Model X", color="White")

    print(c2)
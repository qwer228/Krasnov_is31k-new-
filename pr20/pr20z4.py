class PrivateDictDescriptor:
    def __init__(self, name):
        self.storage_name = f"_{name}"
    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.storage_name)
    def __set__(self, obj, value):
        obj.__dict__[self.storage_name] = value

class D: secret = PrivateDictDescriptor("secret")
d = D()
d.secret = "top"
print(d.secret)          # top
print(d.__dict__)        # {'_secret': 'top'}

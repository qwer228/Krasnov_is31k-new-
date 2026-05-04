class ChangeLogDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        old = self.value
        print(f"Изменение: {old} -> {value}")
        self.value = value

class O: status = ChangeLogDescriptor("off")
o = O()
o.status = "on"  # Изменение: off -> on
o.status = "idle" # Изменение: on -> idle

class User:
    __slots__ = ('login', 'password')
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def change_password(self, old_pass, new_pass):
        if self.password == old_pass:
            self.password = new_pass
            print(" Пароль успешно изменён")
        else:
            print(" Неверный старый пароль")

user = User("admin", "12345")
user.change_password("12345", "newpass")

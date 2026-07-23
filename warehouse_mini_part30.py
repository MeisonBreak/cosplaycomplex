# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: WarehouseMini
class Profile:
    def __init__(self, name="", role="user", warehouse=None):
        self.name = name
        self.role = role
        self.warehouse = warehouse

    def show(self):
        return f"  Профиль [{self.name}] (роль={self.role}, склад={'да' if self.warehouse else 'нет'})"

class ProfileManager:
    profiles = []

    @staticmethod
    def register(name, role="user", warehouse=None):
        p = Profile(name=name, role=role, warehouse=warehouse)
        ProfileManager.profiles.append(p)
        return p

    @staticmethod
    def current():
        if not ProfileManager.profiles:
            ProfileManager.register("default")
        return ProfileManager.profiles[-1]

    @staticmethod
    def switch(name):
        for p in ProfileManager.profiles:
            if p.name == name:
                ProfileManager.profiles.remove(p)
                ProfileManager.profiles.append(p)
                return True
        print(f"  Профиль '{name}' не найден")
        return False

    @staticmethod
    def show_all():
        print("  Все профили:")
        for p in ProfileManager.profiles:
            print(p.show())

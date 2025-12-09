import sys, os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = []
sound_access = []
res_access.append(resource_path("res/models/"))
sound_access.append(resource_path("snd/"))


def change_access(name):
    res_access[0]= os.path.join(base_dir, "..", "res\\") + name + "\\"

    return


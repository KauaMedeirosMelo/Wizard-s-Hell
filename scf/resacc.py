import os

base_dir = os.path.dirname(os.path.abspath(__file__))
res_access = []
res_access.append(os.path.join(base_dir, "..", "res") + "\\" + "models\\")


def change_access(name):
    res_access[0]= os.path.join(base_dir, "..", "res\\") + name + "\\"

    return


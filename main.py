import os


def get_current_dir_content() -> list:

    all_names = os.listdir('.')
    for name in all_names:
        if name == "venv" or name == ".idea":
            all_names.remove(name)
    if "main.py" in all_names:
        all_names.remove("main.py")
    if ".gitignore" in all_names:
        all_names.remove(".gitignore")
    if ".git" in all_names:
        all_names.remove(".git")
    if "README.md" in all_names:
        all_names.remove("README.md")

    return all_names


def copy_files(list):
    destination = os.getcwd()

    for directory in list:
        source = destination + os.path.sep + directory
        all_files = os.listdir(source)
        for f in all_files:
            os.rename(source + os.path.sep + f, destination + os.path.sep + f)


if __name__ == '__main__':
    subDirectories = get_current_dir_content()
    copy_files(subDirectories)





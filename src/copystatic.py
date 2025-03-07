import os
import shutil


def copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        to_path = os.path.join(destination_dir, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files(from_path, to_path)

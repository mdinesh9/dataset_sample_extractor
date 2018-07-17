import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="requires root data path")
parser.add_argument("-d", "--root", type=str, help="pass root directory path")
parser.add_argument("-s", "--sample_size", type=int, help="sample size")
args = vars(parser.parse_args())

# fetch command line arguments
rootdir = args["root"]
sample_count = int(args.get("sample_size")) if args.get("sample_size") else 200

extensions = (".txt",".pdf",".jpeg",".jpg",".png",".gid",".tiff")

def has_files(dir_path):
    files = [file for file in os.listdir(dir_path) 
        if file.endswith(extensions)]

    if len(files) > 0:
        return True
    return False
    

def is_valid(root_dir):
    valid_dirs = set()
    for root, dirs, files in os.walk(root_dir, topdown=False):
        valid = has_files(root)

        if valid:
            valid_dirs.add(root)

    return valid_dirs

def copy_samples(directory):
    rootname = directory.split("/")[0]
    output_dir = directory.replace(rootname, "samples")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    for file in os.listdir(directory)[:sample_count]:
        shutil.copy(os.path.join(directory, file), output_dir)

def start():
    valid_dirs = is_valid(rootdir)

    for directory in valid_dirs:
        copy_samples(directory)

if __name__ == "__main__":
    start()



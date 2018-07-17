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

def has_files():
    pass

def is_valid():
    pass

def copy_samples():
    pass

def start():
    pass

if __name__ == "__main__":
    start()



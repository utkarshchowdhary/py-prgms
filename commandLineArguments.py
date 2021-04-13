import argparse

# Creates Argument Parser object named parser
parser = argparse.ArgumentParser()

# Argument 1: that's a path to a folder
parser.add_argument(
    "--dir", type=str, default="pet_images/", help="path to the folder of pet images"
)  # python check_images.py --dir pet_images/
parser.add_argument(
    "--arch", type=str, default="resnet", help="The CNN model architecture to use"
)
parser.add_argument(
    "--dogfile",
    type=str,
    default="dognames.txt",
    help="The file that contains the list of valid dognames",
)

in_args = parser.parse_args()

# Accesses values of Argument 1 by printing it
print("Argument 1:", in_args.dir)
print("Argument 2:", in_args.arch)
print("Argument 3:", in_args.dogfile)

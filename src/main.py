from normal import normal
from red import red
import sys
import glob

def main():
    args = sys.argv
    if args[1] == "--red" or args[1] == "-r":
        print("Red Image Processing")
        # get image paths
        image_paths = sorted(glob.glob('./data/red/inputs/*.JPG'))
        for image_path in image_paths:
            # process image
            red(image_path,'./data/red/result/')
    
    if args[1] == "--normal" or args[1] == "-n":
        print("Normal Image Processing")
        # get image paths
        image_paths = sorted(glob.glob('./data/normal/inputs/*.JPG'))
        for image_path in image_paths:
            # process image
            normal(image_path,'./data/normal/result/')

if __name__ == "__main__":
    main()

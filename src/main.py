from ant import count_ant
import sys
import glob

RED_IMAGE_PATH = './data/red/inputs/*.JPG'
RED_RESULT_PATH = './data/red/result/'
RED_SMALLEST_AREA = 150
RED_LARGEST_AREA = 4e3

NORMAL_IMAGE_PATH = './data/normal/inputs/*.JPG'
NORMAL_RESULT_PATH = './data/normal/result/'
NORMAL_SMALLEST_AREA = 5e2
NORMAL_LARGEST_AREA = 9e3

def main():
    args = sys.argv
    if args[1] == "--red" or args[1] == "-r":
        print("Red Image Processing")
        # get image paths
        image_paths = sorted(glob.glob(RED_IMAGE_PATH))
        for image_path in image_paths:
            # process image
            count_ant(image_path, RED_RESULT_PATH, RED_SMALLEST_AREA, RED_LARGEST_AREA)
    
    if args[1] == "--normal" or args[1] == "-n":
        print("Normal Image Processing")
        # get image paths
        image_paths = sorted(glob.glob(NORMAL_IMAGE_PATH))
        for image_path in image_paths:
            # process image
            count_ant(image_path, NORMAL_RESULT_PATH, NORMAL_SMALLEST_AREA, NORMAL_LARGEST_AREA)

if __name__ == "__main__":
    main()

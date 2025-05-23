from ant import count_ant
import sys
import glob

RED_IMAGE_PATH = './data/red/inputs/*.JPG'
RED_RESULT_PATH = './data/red/result/'
RED_SMALLEST_AREA = 9e2
RED_LARGEST_AREA = 5e3

NORMAL_IMAGE_PATH = './data/normal/inputs/*.JPG'
NORMAL_RESULT_PATH = './data/normal/result/'
NORMAL_SMALLEST_AREA = 5e2
NORMAL_LARGEST_AREA = 9e3

def main():
    args = sys.argv
    if args[1] == "--red" or args[1] == "-r":
        print("Red Image Processing")
        # Create csv file
        with open(f"{RED_RESULT_PATH}/csv/red.csv", "w", encoding='utf-8') as f:
            f.write("filename,number,total,total_area,diff_of_area,area1,area2,area3,area4,area5,area6,area7,area8,area9,area10,area11,area12,area13,area14,area15\n")
            # Get image paths
            image_paths = sorted(glob.glob(RED_IMAGE_PATH))
            for i, image_path in enumerate(image_paths):
                # Process image
                count_ant(image_path, f, i, RED_RESULT_PATH, RED_SMALLEST_AREA, RED_LARGEST_AREA)
    
    if args[1] == "--normal" or args[1] == "-n":
        print("Normal Image Processing")
        # Create csv file
        with open(f"{NORMAL_RESULT_PATH}/csv/normal.csv", "w", encoding='utf-8') as f:
            f.write("filename,number,total,total_area,diff_of_area,area1,area2,area3,area4,area5,area6,area7,area8,area9,area10,area11,area12,area13,area14,area15\n")
            # Get image paths
            image_paths = sorted(glob.glob(NORMAL_IMAGE_PATH))
            for i, image_path in enumerate(image_paths):
                # Process image
                count_ant(image_path, f, i, NORMAL_RESULT_PATH, NORMAL_SMALLEST_AREA, NORMAL_LARGEST_AREA)

if __name__ == "__main__":
    main()

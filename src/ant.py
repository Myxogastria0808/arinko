from utils.divide import divide_process
from utils.whole import whole_process

def count_ant(image_path, output_path, smallest_area, largest_area):
    print("-------------------------------------------")
    print(f"image path: {image_path}.")
    # Process whole image
    ant_count = whole_process(image_path, output_path, smallest_area, largest_area)
    # Process divided image
    div_total_ant_count = divide_process(image_path, output_path, smallest_area, largest_area)

    # Show total ant quantity
    print(f"total ant quantity: {ant_count}.")
    # Show div total ant quantity
    print(f"div total ant quantity: {div_total_ant_count}, diff: {div_total_ant_count - ant_count}.")
    print("-------------------------------------------")

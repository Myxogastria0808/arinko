from utils.divide import divide_process
from utils.whole import whole_process

def count_ant(image_path, f, number, output_path, smallest_area, largest_area):
    print("-------------------------------------------")
    print(f"image path: {image_path}.")
    # Process whole image
    total_ant_count = whole_process(image_path, output_path, smallest_area, largest_area)
    # Process divided image
    div_total_ant_count, div_ant_counts = divide_process(image_path, output_path, smallest_area, largest_area)
    # Write to csv file
    f.write(f"{image_path},{number},{total_ant_count},{div_total_ant_count},{total_ant_count - div_total_ant_count}")
    for div_ant_count in div_ant_counts:
        f.write(f",{div_ant_count}")
    f.write("\n")
    
    # Show total ant quantity
    print(f"total ant quantity: {total_ant_count}.")
    # Show div total ant quantity
    print(f"div total ant quantity: {div_total_ant_count}, diff: {total_ant_count - div_total_ant_count}.")
    print("-------------------------------------------")

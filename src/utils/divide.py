import cv2
import os
from utils.pre import pre_process

def divide_process(image_path, output_path, smallest_area, largest_area):
    # Pre process
    trimming, threshold = pre_process(image_path)
    
    # Initialize total ant count
    div_total_ant_count = 0
    # Initialize div ant counts
    div_ant_counts = []
    # Get height and width
    height, width = threshold.shape
    # Divide the image into 15 parts
    for div_width in range(0, 3, 1):
        for div_height in range(0, 5, 1):
            div_trimming = trimming[height // 5 * div_height : height // 5 * (div_height + 1),  width // 3 * div_width : width // 3 *  (div_width + 1)]
            div_threshold = threshold[height // 5 * div_height : height // 5 * (div_height + 1),  width // 3 * div_width : width // 3 *  (div_width + 1)]
            # Find contours (輪郭抽出)
            # 参考サイト: https://www.codevace.com/py-opencv-findcontours/
            contours, _ = cv2.findContours(div_threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            # Draw contours (輪郭描画)
            div_contours_image = trimming.copy()
            cv2.drawContours(div_contours_image, contours, -1, color=(0, 255, 0), thickness=2)
            # Save
            output_image_name = os.path.split(image_path)[1].split('.')[0] + f'-{div_width}-{div_height}.JPG'
            cv2.imwrite(f'{output_path}/divide/{output_image_name}', div_trimming)
            
            # Draw rectangle (短形描画)
            # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
            # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
            # rectangle quantity
            div_ant_count = 0
            # Process each contour
            for contour in contours:
                # Get bounding box
                x, y, w, h = cv2.boundingRect(contour)
                # Get contour area
                area = cv2.contourArea(contour)
                # Remove noise
                # 参考サイト: https://nanjamonja.net/archives/171
                # Draw rectangle
                if smallest_area < area < largest_area:
                    # Ignore small and large area
                    cv2.rectangle(trimming, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Count rectangle
                    div_ant_count += 1
            # Append div ant count
            div_ant_counts.append(div_ant_count)
            # Add to div total ant count
            div_total_ant_count += div_ant_count
            # Show total ant quantity
            print(f"height: {div_height}, width: {div_width}, each ant quantity: {div_ant_count}.")
    
    return div_total_ant_count, div_ant_counts

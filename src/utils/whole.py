import cv2
import os
from utils.pre import pre_process

def whole_process(image_path, output_path, smallest_area, largest_area):
    # Pre process
    trimming, threshold = pre_process(image_path)
    
    # Find contours (輪郭抽出)
    # 参考サイト: https://www.codevace.com/py-opencv-findcontours/
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    # Draw contours (輪郭描画)
    contours_image = trimming.copy()
    cv2.drawContours(contours_image, contours, -1, color=(0, 255, 0), thickness=2)
    
    # Draw rectangle (短形描画)
    # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
    # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
    # rectangle quantity
    total_ant_count = 0
    
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
            total_ant_count += 1
        # Draw all rectangles
        cv2.rectangle(contours_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Save
    output_image_name = os.path.split(image_path)[1]
    cv2.imwrite(f'{output_path}/{output_image_name}', trimming)
    
    return total_ant_count

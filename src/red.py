import cv2
import os

def red(image_path, output_path):
    # Load (画像読み込み)
    image = cv2.imread(image_path)

    # Trimming (トリミング)
    # [top : bottom, left : right]
    trimming = image[0 : 4176, 200: 3500]

    # Mask (マスク)
    # 参考サイト: https://qiita.com/takiguchi-yu/items/277c596b7f96b0d9f9c0
    # [top : bottom, left : right]
    trimming[800:1200, 600:1000] = 255
    trimming[1800:2200, 200:700] = 255
    trimming[2900:3300, 600:1000] = 255

    # Grayscale (グレースケール化)
    grayscale = cv2.cvtColor(trimming, cv2.COLOR_BGR2GRAY)

    # # Remove noise using Gaussian blur (ノイズ除去)
    # noise = cv2.GaussianBlur(grayscale, (5, 5), 0)
    # cv2.imwrite('./data/red/noise.jpg', noise)

    # Threshold (二値化)
    _, threshold = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)

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
    ant_count = 0
    # process each contour
    for contour in contours:
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        # Get contour area
        area = cv2.contourArea(contour)
        # Remove noise
        # 参考サイト: https://nanjamonja.net/archives/171
        # Draw rectangle
        if 150 < area < 4e3:
            # Ignore small and large area
            cv2.rectangle(trimming, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # count rectangle
            ant_count += 1
        # Draw all rectangles
        cv2.rectangle(contours_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show total ant quantity
    print(f"image_path: {image_path}, total ant quantity: {ant_count}.")

    # Save
    output_image_name = os.path.split(image_path)[1]
    cv2.imwrite(f'{output_path}/{output_image_name}', trimming)

    # Process divided image
    height, width = threshold.shape
    div_total_ant_count = 0
    # Divide the image into 15 parts
    for div_width in range(0, 3, 1):
        for div_height in range(0, 5, 1):
            divided_trimming = trimming[height // 5 * div_height : height // 5 * (div_height + 1),  width // 3 * div_width : width // 3 *  (div_width + 1)]
            divided_threshold = threshold[height // 5 * div_height : height // 5 * (div_height + 1),  width // 3 * div_width : width // 3 *  (div_width + 1)]
            # Find contours (輪郭抽出)
            # 参考サイト: https://www.codevace.com/py-opencv-findcontours/
            contours, _ = cv2.findContours(divided_threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            # Draw contours (輪郭描画)
            divided_contours_image = trimming.copy()
            cv2.drawContours(divided_contours_image, contours, -1, color=(0, 255, 0), thickness=2)
            # Save
            output_image_name = os.path.split(image_path)[1].split('.')[0] + f'-{div_width}-{div_height}.JPG'
            cv2.imwrite(f'{output_path}/divide/{output_image_name}', divided_trimming)
            
            # Draw rectangle (短形描画)
            # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
            # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
            # rectangle quantity
            div_ant_count = 0
            # process each contour
            for contour in contours:
                # Get bounding box
                x, y, w, h = cv2.boundingRect(contour)
                # Get contour area
                area = cv2.contourArea(contour)
                # Remove noise
                # 参考サイト: https://nanjamonja.net/archives/171
                # Draw rectangle
                if 150 < area < 4e3:
                    # Ignore small and large area
                    cv2.rectangle(trimming, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # count rectangle
                    div_ant_count += 1
            # Add to div total ant count
            div_total_ant_count += div_ant_count
            # Show total ant quantity
            print(f"height: {div_height}, width: {div_width}, each ant quantity: {div_ant_count}.")
    # Show div total ant quantity
    print(f"image_path: {image_path}, div total ant quantity: {div_total_ant_count}, diff: {div_total_ant_count - ant_count}.")

import cv2
import os

def normal(image_path, output_path):
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

    # Threshold (二値化)
    # 参考サイト: https://qiita.com/tokkuri/items/ad5e858cbff8159829e9
    _, threshold = cv2.threshold(grayscale, 90, 255, cv2.THRESH_BINARY)

    # Find contours (輪郭抽出)
    # 参考サイト: https://www.codevace.com/py-opencv-findcontours/
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Draw contours (輪郭描画)
    contours_image = trimming.copy()

    # Draw rectangle (短形描画)
    # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
    # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
    # rectangle quantity
    detect_count = 0
    # process each contour
    for contour in contours:
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        # Get contour area
        area = cv2.contourArea(contour)
        # Remove noise
        # 参考サイト: https://nanjamonja.net/archives/171
        # Draw rectangle
        if 5e2 < area < 9e3:
            # Ignore small and large area
            cv2.rectangle(trimming, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # count rectangle
            detect_count += 1
        # Draw all rectangles
        cv2.rectangle(contours_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show detected count
    print(f"image_path: {image_path}, ant: {detect_count}.")

    # Save
    output_image_name = os.path.split(image_path)[1]
    cv2.imwrite(f'{output_path}/{output_image_name}', trimming)

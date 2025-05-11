import cv2

def normal():
    # Load (画像読み込み)
    image_path = './data/normal/sample.png'
    image = cv2.imread(image_path)

    # Grayscale (グレースケール化)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./data/normal/grayscale.jpg', grayscale)

    # Remove noise using Gaussian blur (ノイズ除去)
    # noise = cv2.GaussianBlur(grayscale, (5, 5), 0)
    # cv2.imwrite('./data/normal/noise.jpg', noise)

    # Threshold (二値化)
    # 参考サイト: https://qiita.com/tokkuri/items/ad5e858cbff8159829e9
    _, threshold = cv2.threshold(grayscale, 110, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./data/normal/threshold.jpg', threshold)

    # Find contours (輪郭抽出)
    # 参考サイト: https://www.codevace.com/py-opencv-findcontours/
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Draw contours (輪郭描画)
    contours_image = image.copy()
    cv2.drawContours(contours_image, contours, -1, color=(0, 255, 0), thickness=2)
    cv2.imwrite('./data/normal/contours.jpg', image)

    # Draw rectangle (短形描画)
    # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
    # 参考サイト: https://qiita.com/neriai/items/448a36992e308f4cabe2
    # rectangle quantity
    detect_count = 0
    # process each contour
    for contour in contours:
        # Get contour area
        area = cv2.contourArea(contour)
        # Remove noise
        # 参考サイト: https://nanjamonja.net/archives/171
        if area < 5e2 or 4e3 < area:
            continue
        detect_count += 1
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        # Draw rectangle
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show detected count
    print(f"Detected {detect_count} rectangles.")

    # Save
    cv2.imwrite('./data/normal/result.jpg', image)

import cv2

def red():
    # Load (画像読み込み)
    image_path = './data/red/sample.jpg'
    image = cv2.imread(image_path)

    # Trimming (トリミング)
    # [top : bottom, left : right]
    trimming = image[0 : 4176, 200: 3500]
    cv2.imwrite("./data/red/trimming.jpg", trimming)

    # Mask (マスク)
    # 参考サイト: https://qiita.com/takiguchi-yu/items/277c596b7f96b0d9f9c0
    # [top : bottom, left : right]
    trimming[800:1200, 600:1000] = 255
    trimming[1800:2200, 200:700] = 255
    trimming[2900:3300, 600:1000] = 255
    cv2.imwrite('./data/red/mask.jpg', trimming)

    # Grayscale (グレースケール化)
    grayscale = cv2.cvtColor(trimming, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./data/red/grayscale.jpg', grayscale)

    # # Remove noise using Gaussian blur (ノイズ除去)
    # noise = cv2.GaussianBlur(grayscale, (5, 5), 0)
    # cv2.imwrite('./data/red/noise.jpg', noise)

    # Threshold (二値化)
    _, threshold = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./data/red/threshold.jpg', threshold)

    # Find contours (輪郭抽出)
    # 参考サイト: https://www.codevace.com/py-opencv-findcontours/
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Draw contours (輪郭描画)
    contours_image = trimming.copy()
    cv2.drawContours(contours_image, contours, -1, color=(0, 255, 0), thickness=2)
    cv2.imwrite('./data/red/contours.jpg', contours_image)

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
        if 1e2 < area < 4e3:
            # Ignore small and large area
            cv2.rectangle(trimming, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # count rectangle
            detect_count += 1
        # Draw all rectangles
        cv2.rectangle(contours_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # contours and rectangle
    cv2.imwrite('./data/red/contours_rectangle.jpg', contours_image)
    
    # Show detected count
    print(f"Detected {detect_count} rectangles.")

    # Save
    cv2.imwrite('./data/red/result.jpg', trimming)

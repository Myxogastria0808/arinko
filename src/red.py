import cv2

def red():
    # Load (画像読み込み)
    image_path = './data/red/sample.jpg'
    image = cv2.imread(image_path)

    # Grayscale (グレースケール化)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('./data/red/grayscale.jpg', grayscale)

    # # Remove noise using Gaussian blur (ノイズ除去)
    # noise = cv2.GaussianBlur(grayscale, (5, 5), 0)
    # cv2.imwrite('./data/red/noise.jpg', noise)

    # Threshold (二値化)
    _, threshold = cv2.threshold(grayscale, 50, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./data/red/threshold.jpg', threshold)

    # Find contours (輪郭抽出)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Draw contours (輪郭描画)
    contours_image = image.copy()
    cv2.drawContours(contours_image, contours, -1, color=(0, 255, 0), thickness=2)
    cv2.imwrite('./data/red/contours.jpg', image)

    # Draw rectangle (短形描画)
    # rectangle quantity
    detect_count = 0
    # process each contour
    for contour in contours:
        # Get contour area
        area = cv2.contourArea(contour)
        # Remove noise
        if area < 1e2 or 4e3 < area:
            continue
        detect_count += 1
        # Get bounding box
        x, y, w, h = cv2.boundingRect(contour)
        # Draw rectangle
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Show detected count
    print(f"Detected {detect_count} rectangles.")

    # Save
    cv2.imwrite('./data/red/result.jpg', image)

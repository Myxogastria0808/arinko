import cv2

def pre_process(image_path):
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

    return trimming, threshold

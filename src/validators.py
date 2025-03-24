

def validate_image_url(image_url):
    img_xt = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"]

    return any(ext in image_url for ext in img_xt)

def validate_url(url):
    url_xt = ["http", "//"]

    return any(ext in url for ext in url_xt)
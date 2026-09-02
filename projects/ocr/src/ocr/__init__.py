from rapidocr import RapidOCR

def main() -> None:
    engine = RapidOCR()
    img_path_or_url = "./data/homelab.png"
    result = engine(img_path_or_url)
    print(result)

    result.vis("./data/homelab_result.png")
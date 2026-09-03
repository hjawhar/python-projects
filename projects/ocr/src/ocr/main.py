from rapidocr import RapidOCR

def main() -> None:
    print("Starting OCR")
    engine = RapidOCR()
    result = engine("./data/homelab.png")
    print(result)
    result.vis("./data/homelab_result.png")

if __name__ == "__main__":
    main()
import qrcode


def generate_code(data, filename):
    image = qrcode.make(data)
    image.save(f"{filename}.png")

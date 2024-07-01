import qrcode
img = qrcode.make('who are u')
type(img)  # qrcode.image.pil.PilImage
img.save("who.png")
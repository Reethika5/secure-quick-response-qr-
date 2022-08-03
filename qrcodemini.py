from asyncio.windows_events import ERROR_CONNECTION_ABORTED
from ensurepip import version
from turtle import fillcolor
import qrcode  

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=30,border=2)
qr.add_data("https://www.netflix.com/in/")
qr.make(fit=True)

img = qr.make_image(fill_color="blue",back_color="white")
img.save("advanced.png")
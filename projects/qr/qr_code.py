import qrcode as qr 

img = qr.make("https://github.com/aditya1q/python_basics")
img.save('git_qr.png')
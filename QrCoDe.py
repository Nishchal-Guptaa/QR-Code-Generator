import qrcode

img = qrcode.make(input("Enter the link: "))
# img.save('myQRcode.png')
img.show()
print(img)
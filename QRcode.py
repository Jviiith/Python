# How to convert text/link/url into a QR code
# install libraries needed: qrcode & Image
# create a function that collects a text and convert it into a qrcode
# save qrcode as an image
# run the function
import qrcode


def generate_qrcode(link):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qrimg.png')


url = input('Enter your URL link: ')
generate_qrcode(url)

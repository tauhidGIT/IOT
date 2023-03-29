#Import lib
import wifi_qrcode_generator as qr
import config

# Use wifi_qrcode() to create a QR image
qrCode = qr.wifi_qrcode(config.ssid, False, 'WPA', config.password)

# Display the qrImage
qrCode.show()

# Save the image as PNG file
qrCode.save("my_wifi_qr.png")
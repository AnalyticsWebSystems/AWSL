"""
This is a free qr generator, we will use it for our website
"""

import qrcode

s = "https://github.com/BoltDreamzz?tab=repositories"
v = "https://dreamapp-hbpq.onrender.com/splash"
url = qrcode.make(v)
url.save("myQrcode.png")
url.show()

# url.svg("myqr.svg", scale=8)
#
# pboy = url.png("myqr.png", scale=6)
# print(pboy)
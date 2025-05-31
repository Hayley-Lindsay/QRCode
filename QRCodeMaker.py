#Import QRcode with pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
#String that represents the qr code
QR = "https://disneyland.disney.go.com/?ef_id=550c3fd8c8bd1ecdea6057e39b9bb414:G:s&s_kwcid=AL!5054!10!79989658982085!!!!79989836056350!!650163217!1279832835816306&CMP=KNC-FY25_DLR_TRA_DOM_LACN_SCP_SCP_365Scope_EXACT%7CB%7C5252059.DL.AM.01.02%7CM1GW875%7CBR%7C79989658982085&keyword_id=kwd-79989836056350:loc-71265%7Cdc%7Cdisneyland%7C79989658982085%7Ce%7C5054:10%7C&msclkid=550c3fd8c8bd1ecdea6057e39b9bb414"
#Generate QR code
url = pyqrcode.create(QR)
#Create and save the svg file named myQRCODE.svg
url.svg("myQRCode.svg", scale=8)
#Create and save the png file named myQRCODE.png
url.png("myQRCode.png", scale=8)

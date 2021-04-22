import webbrowser
import sys
import pyperclip

# todo: read command line arguments ie ['mapit.py','870','Valencia','St.']
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/870 Valencia St.
url = "https://www.google.com/maps/place/"
webbrowser.open(url + address)

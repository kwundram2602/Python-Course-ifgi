from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtWebKitWidgets import QWebView

url = "https://de.wikipedia.org/wiki/[%Name%]"
qweb = QWebView()
qweb.load(QUrl(url))
qweb.show()
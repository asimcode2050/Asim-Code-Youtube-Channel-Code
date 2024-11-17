import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor


class SecureBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Secure Web Browser By Asim Code')
        self.setGeometry(100, 100, 1200, 800)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        self.address_bar = QLineEdit(self)
        self.address_bar.setPlaceholderText("Enter URL here...")
        self.address_bar.returnPressed.connect(self.load_url)
        layout.addWidget(self.address_bar)
        self.browser = QWebEngineView(self)
        layout.addWidget(self.browser)
        profile = QWebEngineProfile.defaultProfile()
        interceptor = RequestInterceptor()
        profile.setRequestInterceptor(interceptor)
        self.browser.setUrl(QUrl('https://www.google.com'))

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith('http'):
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))


class RequestInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, request):
        url = request.url().toString()
        if 'example.com' in url:
            print(f"Blocked access to: {url}")
            request.setUrl(QUrl('about:blank'))  # Prevent loading this site
        else:
            request.setUrl(request.url())  # Allow other URLs


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecureBrowser()
    window.show()
    sys.exit(app.exec_())

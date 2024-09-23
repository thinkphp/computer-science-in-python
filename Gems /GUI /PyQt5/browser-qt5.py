import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QLineEdit, QProgressBar, QToolBar, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Qt Browser By Adrian Statescu")
        self.setGeometry(100, 100, 1024, 768)

        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)

        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.create_toolbar()
        self.add_new_tab()  # Add the first tab

    def create_toolbar(self):
        navigationBar = QToolBar()
        self.addToolBar(navigationBar)

        self.back_button = QAction('←', self)
        self.back_button.triggered.connect(self.back)
        navigationBar.addAction(self.back_button)

        self.forward_button = QAction('→', self)
        self.forward_button.triggered.connect(self.forward)
        navigationBar.addAction(self.forward_button)

        reload_button = QAction('↻', self)
        reload_button.triggered.connect(self.reload)
        navigationBar.addAction(reload_button)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigate_to_url)
        navigationBar.addWidget(self.urlBar)

        go_button = QPushButton('Go')
        go_button.clicked.connect(self.navigate_to_url)
        navigationBar.addWidget(go_button)

        new_tab_button = QPushButton('New Tab')
        new_tab_button.clicked.connect(lambda: self.add_new_tab())
        navigationBar.addWidget(new_tab_button)

        self.progress = QProgressBar(self)
        navigationBar.addWidget(self.progress)

    def add_new_tab(self, qurl=None):
        if qurl is None:
            qurl = QUrl('http://www.bing.com')
        elif isinstance(qurl, str):
            qurl = QUrl(qurl)

        # Check if qurl is a valid QUrl object
        if not isinstance(qurl, QUrl):
            print("Error: qurl is not a QUrl instance.")
            return

        print(f"Adding new tab with URL: {qurl}")  # Debugging output

        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabWidget.addTab(browser, "New Tab")
        
        # Connect URL change and load finish signals
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser))
        browser.loadFinished.connect(lambda success, i=i, browser=browser: 
            self.tabWidget.setTabText(i, browser.page().title()) if success else print("Failed to load")
        )
        browser.loadStarted.connect(lambda: self.progress.setValue(0))
        browser.loadFinished.connect(lambda _, browser=browser: self.progress.setValue(100))

        self.tabWidget.setCurrentIndex(i)
        self.urlBar.setText(qurl.toString())

    def current_browser(self):
        return self.tabWidget.currentWidget()

    def back(self):
        self.current_browser().back()

    def forward(self):
        self.current_browser().forward()

    def reload(self):
        self.current_browser().reload()

    def navigate_to_url(self):
        q = QUrl(self.urlBar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.current_browser().setUrl(q)

    def update_urlbar(self, q, browser=None):
        if browser != self.current_browser():
            return
        self.urlBar.setText(q.toString())
        self.urlBar.setCursorPosition(0)

    def close_tab(self, i):
        if self.tabWidget.count() < 2:
            return
        self.tabWidget.removeTab(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())


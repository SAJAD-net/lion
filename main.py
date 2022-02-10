import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from lion import Ui_Form

class mcWidget(QtWidgets.QWidget):
    def __init__(self):
        super(mcWidget, self).__init__()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

class browserApp(mcWidget, Ui_Form):
    def __init__(self):
        super(browserApp, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.newShowMaximized)
        self.lineEdit.returnPressed.connect(self.load)
        self.pushButton_4.clicked.connect(self.backward)
        self.pushButton_5.clicked.connect(self.forward)
        self.pushButton_6.clicked.connect(self.reload)
        
        home = QtCore.QUrl("https://duckduckgo.com")
        self.webEngineView.load(home)

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)
            if self.webEngineView.urlChanged:
            	self.lineEdit.setText(url.toString())

    def newShowMaximized(self):
        if self.pushButton_3.isChecked():
            self.showMaximized()
        else:
            self.showNormal()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = browserApp()
    Form.show()
    sys.exit(app.exec_())

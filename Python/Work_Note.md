### Monkey Patch

__Create monkey with parameters:__

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

def resize_event(self: QMainWindow, event):
    width = event.size().width()
    height = int(width/self.w_proportion * self.h_proportion)
    self.resize(width, height)

class App(QApplication):

    def __init__(self, *args, main_page = QUrl("https://www.baidu.com"), **kwargs):
        super().__init__(*args, **kwargs)
        self._mainwindow = QMainWindow()
        self._webview = QWebEngineView()
        self._layout = QVBoxLayout()
        self._mainwindow.w_proportion, self._mainwindow.h_proportion = 16, 10
        self._mainwindow.resizeEvent = lambda event: resize_event(self._mainwindow, event)
```

__Annotation:__

Create monkey patch using for handle resize event(keep the height-width proportion), that means this function will be called when the user resize the windows.

But it just a demonstration and in fact, it will cause a bug because QT will resize the window continually if the `resize` function parameter `w` & `h` are unsuitable. And QT will be caught in a endless loop, which'll make the application unresponsive.

Here is the error code:
`QWindowsWindow::setGeometry: Unable to set geometry 1920x1200+0+23 (frame: 1936x1239-8-8) on QWidgetWindow/"QMainWindowClassWindow" on "HP V22 (1)". Resulting geometry: 1920x1061+0+23 (frame: 1936x1100-8-8) margins: 8, 31, 8, 8)`

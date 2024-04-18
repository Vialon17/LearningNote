# Work Note

Write Some Note About Work Is A Good Idea. _-- By Vialon17_

**Intro:** After reviewed the past half year work, though learned many coding skills and work frames, like `Vue`, `PySide`, `Flask`, `SqlAlchemy`, but there have some other important core skills that I need learn. So I write this work note to record my work and some useful code information.

**And May You Get Something Useful Here. :)**

**Catalogue**: 

* [`Python`](#python-note): [`Flask`](#flask-note), [`PySide(QT)`](#pyside-note), [`Pandas`](#pandas-note), [`Python`](#python-note-1), [`Utils`](#utils-note)

* [`JavaScript`](#js-note): [`Vue`](#vue-note), [`JavaScript`](#javascript-note)

* [`Note:`](#note-note)

------

## Python Note


### Flask Note

### PySide Note

### Pandas Note

### Python Note

#### Monkey Patch

`Monkey Patch` is a special program language feature, and it will allow user add some patchs to existed object to correct some bugs. Here I write a demonstration to fix the windows aspect ratio when user resize window for QT.

__Create monkey with parameters:__

```python
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl


def resize_event(self: QMainWindow, event):
    width = event.size().width()
    height = int(width/self.w_proportion * self.h_proportion)
    print(width, height)
    self.resize(width, height)

class App(QApplication):

    def __init__(self, *args, main_page = QUrl("https://www.baidu.com"), **kwargs):
        super().__init__(*args, **kwargs)

        self._webview = QWebEngineView()
        self._webview.setUrl(main_page)

        self._mainwindow = QMainWindow()
        self._mainwindow.w_proportion, self._mainwindow.h_proportion = 8, 6

        # assgin the resize event to 
        self._mainwindow.resizeEvent = lambda event: resize_event(self._mainwindow, event)
        self._mainwindow.setCentralWidget(self._webview)
        self._mainwindow.show()

if __name__ == '__main__':
    app = App()
    sys.exit(app.exec())
```

__Annotation:__

Create monkey patch using for handle resize event(keep the height-width proportion), that means this function will be called when the user resize the windows.

### Utils Note

## JS Note

### Vue Note

### JavaScript Note

## Note Note

.
..
.
.
.
.
.
.
.
.
.
.
.
.

.
.
.
.
.
.
.
.
.

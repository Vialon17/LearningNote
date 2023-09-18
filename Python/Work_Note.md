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


### Flask Initialization

Flask deleted the decorator `before_first_request` in its 2.3.3 version, so here uses the `before_request` and set `flask.config` dictorary variable to simulate the former.

```python
app = Flask(__name__)
coms_cursor = None

@app.before_request
def before_first_request():
    global coms_cursor
    if not app.config['APP_ALREADY_STARTED']:
        coms_cursor = Coms("config.json")
        app.config['APP_ALREADY_STARTED'] = True

if __name__ == "__main__":
    app.config['APP_ALREADY_STARTED'] = False
    app.run(host = "localhost", port = 8080, debug = True)
```

It'll run the `before_first_request` function code and adjust the configuration

### Flask CORS(Cross-Origin Resource Sharing)

When the request server posts a request to a server under different protocols, domains and ports, there comes the CORS -- the server or the browser defaultly refuse the cross-origin request to protect it self, but for this program, we need the web get the serial infomation and transport info between different server, so it's necessary to cancel the restrict for the request server.

Command --> `pip isntall Flask-cors`

__Method_1:__ use decorator `cross_origin` to assign specific route function to deal with cors error.

```python
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
@app.route("/")
@cross_origin(origins = "request_server_ip", methods = ['get', 'post'])
def parse_function():
    print("123")
if __name__ == "__main__":
    app.run("0.0.0.0", port = 8080, debug = True)
```

__Method_2:__ use class `CROS` instance and pass the flask instance to it.

```python
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)

@app.route("/")
def parse_function():
    print("123")
if __name__ == "__main__":
    CORS(app)
    app.run("0.0.0.0", port = 8080, debug = True)
```

But I don't like the second way because of its security policy, it seems like accept all requests from any domains...

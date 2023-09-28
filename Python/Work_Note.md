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

--------

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

It'll run the `before_first_request` function code and adjust the configuration.

-------

### Flask CORS(Cross-Origin Resource Sharing)

When the request server posts a request to a server under different protocols, domains and ports, there comes the CORS -- the server or the browser defaultly refuse the cross-origin request to protect it self, but for this program, we need the web get the serial infomation and transport info between different server, so it's necessary to cancel the restrict for the request server.

Command --> `pip isntall flask-cors`

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

--------

### Return Ternary Operator

We have the functioin to extract the alphabetic and digital info:
```python
def split_string(input_string: str):
    string_type, string_minnum, string_maxnum = [\
        re.findall(i, input_string) for i in \
            [r"[A-Za-z]+", r"[\d]+$|[\d+]+\.{0}", r"\.(\d+)"]]

    string_type, string_maxnum = string_type[0], string_maxnum[0]
    if len(string_minnum) == 3:
        string_float, string_minnum = string_minnum[2], string_minnum[0]
    else:
        string_minnum = string_minnum[0]
    return string_type, string_float if "string_float" in vars() \
        else string_type
```

But in fact, it return `string_type` twice and makes unnecessary duplication, this confused me for serveral hours to find tbe bug, and finally tried the `dis` module to analyse the code, here is the result:

```python
from dis import dis
dis(split_string)

# result
 23           0 LOAD_CLOSURE             0 (input_string)
              2 BUILD_TUPLE              1
              4 LOAD_CONST               1 (<code object <listcomp> at 0x00000234439890B0, file "temp.py", line 23>)
              6 LOAD_CONST               2 ('split_string.<locals>.<listcomp>')
              8 MAKE_FUNCTION            8 (closure)

 25          10 LOAD_CONST               3 (('[A-Za-z]+', '[\\d]+$|[\\d+]+\\.{0}', '\\.(\\d+)'))

 23          12 GET_ITER
             14 CALL_FUNCTION            1
             16 UNPACK_SEQUENCE          3
             18 STORE_FAST               1 (string_type)
             20 STORE_FAST               2 (string_minnum)
             22 STORE_FAST               3 (string_maxnum)

 27          24 LOAD_FAST                1 (string_type)
             26 LOAD_CONST               4 (0)
             28 BINARY_SUBSCR
             30 LOAD_FAST                3 (string_maxnum)
             32 LOAD_CONST               4 (0)
             34 BINARY_SUBSCR
             36 ROT_TWO
             38 STORE_FAST               1 (string_type)
             40 STORE_FAST               3 (string_maxnum)

 28          42 LOAD_GLOBAL              0 (len)
             44 LOAD_FAST                2 (string_minnum)
             46 CALL_FUNCTION            1
             48 LOAD_CONST               5 (3)
             50 COMPARE_OP               2 (==)
             52 POP_JUMP_IF_FALSE       36 (to 72)

 29          54 LOAD_FAST                2 (string_minnum)
             56 LOAD_CONST               6 (2)
             58 BINARY_SUBSCR
             60 LOAD_FAST                2 (string_minnum)
             62 LOAD_CONST               4 (0)
             64 BINARY_SUBSCR
             66 ROT_TWO
             68 STORE_FAST               4 (string_float)
             70 STORE_FAST               2 (string_minnum)

 30     >>   72 LOAD_FAST                1 (string_type)
             74 LOAD_CONST               7 ('string_float')
             76 LOAD_GLOBAL              1 (vars)
             78 CALL_FUNCTION            0
             80 CONTAINS_OP              0
             82 POP_JUMP_IF_FALSE       45 (to 90)
             84 LOAD_FAST                4 (string_float)
             86 BUILD_TUPLE              2
             88 RETURN_VALUE
        >>   90 LOAD_FAST                1 (string_type)
             92 BUILD_TUPLE              2
             94 RETURN_VALUE

Disassembly of <code object <listcomp> at 0x00000234439890B0, file "temp.py", line 23>:
 23           0 BUILD_LIST               0
              2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 8 (to 22)

 24           6 STORE_FAST               1 (i)
              8 LOAD_GLOBAL              0 (re)
             10 LOAD_METHOD              1 (findall)
             12 LOAD_FAST                1 (i)
             14 LOAD_DEREF               0 (input_string)
             16 CALL_METHOD              2

 23          18 LIST_APPEND              2
             20 JUMP_ABSOLUTE            2 (to 4)
        >>   22 RETURN_VALUE
```

Pay attention to the 30th row:

* operation 72 -- load variable `string_type`
* operation 74-80 -- create condition sentence and get the result
* operation 82 -- accoring to the condition, jump to the 90th
* operation 90 -- __load variable `string_type`__ _(duplicated)_
* operation 92&94 -- build tuple and return result

So there comes the reason: the ternary operator never take care of the `,` punctation, it just work for the sentence before itself.

We need rewrite the return code:`return (string_type, string_float) if "string_float" in vars() else string_type`.

-------

# PySerial Communication

Different from post order and get info from the lower, data receiving frequency is important for the lower that will post data to the upper automatically.

```python
a = [5,0,53,6] + list(check_crc([5,0,53,6]))
coms_cursor = Coms("config.json")
count = 0
while count <= 10000:
    temp_info = coms_cursor.alarm.read_all()
    print(temp_info, count)
    count += 1
    sleep(0.5) # the read frequency
coms_cursor.alarm.close()
```

Reading data once per second `sleep(1)` will lead to the lower computer overheat and the posting data unstably, but when set the reading frequency twice per second, it won't result in this.

I personally think this mainly caused by the lower `cache monery leaks`: If receiving data with slow frequency, the lower computer CPU will need to wipe superfluous data and re-write data to the cache memory, compared with writing data to the cache(the previous data has been transmitted to the upper), the slow frequency will do more CPU calculation.

In fact, other applications that communicate with the serial lower computer always set the default read frequency one thousand times per second.

-------

### QT Customized Signal and Slot(PySide6)

It's necessary to create customized signal and slot in QT system to face different user requirements.
```python
from PySide6.QtCore import Slot, QThread, Signal

class App(QApplication):

    # Signal part
    _warn = Signal(str, bool)
    _clipboard = Signal(str)

    def __init__(self, *other, **others):
        self._warn.connect(self._warn_box)
        self._clipboard.connect(self._copy_clipboard)
        ...

    def run_end(self):
        self._warn.emit("ByeBye!", True)

    def run_copy(self, data: str):
        self._clipboard.emit("https://github.com/Vialon17/LearningNote/edit/main/Python/Work_Note.md")

    @Slot()
    def _warn_box(self, message；str, end: bool = False):
        message_box = QMessageBox()
        message_box.setFixedSize(300, 200)
        message_box.setWindowTitle("Warning!")
        message_box.setText(message)
        if end:
            sys.exit(0)

    @Slot()
    def _copy_clipboard(self, info: str):
        import pyperclip
        pyperclip.copy(text)
```

This example creates an application and defines two signal `warn` and `clipboard`, two slot function `_warn_box` and `_copy_clipboard`, in its initiation function, we connect the signals and slots together.

* Signal variable will create rule about its emit type.

    the _warn signal can just emit two parameter -- string and bool

__Attention__: 

The signal variables must be defined in QT system class environment and shouldn't be putted in `__init__` function. the QTCore.Signal class just creates a signal instance just when it has checked out itself in QT system class.

And the Signal & Slot mechanism can be used in different threads, which means u can submit an info to a signal variable and call its slot functions.

# The Magic Method

_-- The Characteristic Methods Of Python, Syntax Sugers._

----

Let English be your coding language!

## The Catalog
- [**The Magic Method**](#the-magic-method)
  - [**The Catalog**](#the-catalog)
  - [**\_\_init__**](#\_\_init__)
  - [**\_\_new__**](#\_\_init__)


## \_\_init__

__Original Word: Initiation__

Brief Intro: \_\_init__() method usually used for _class_ instance initiation, it won't return variables and info.

__The Process Of Python _Class_ Creates Instance:__

Any _class_ is the subclass of _Object_ -- the basic class in Python. An instance of the class is created by calling the class as if it were a function. This triggers the \_\_new__ and \_\_init__ methods. 

Firstly, the Python interpreter will call the target class \_\_new__() method -- the static method offered by the baisc Object class, there have two purposes:

* Allocate memory storage for the new class instance;

* Return the new instance pointer object;

```python
# the default __new__() method
# the defaulter won't handle any parameter

class MyClass(Object):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

```
_Addition: Through re-write the \_\_new\_\_ method, we can implement singleton pattern._

```python
# the singleton pattern class
# this class will only create one instance, and will return this instance whenever it's called
class Single:

    def __new__(cls):
        instance = None
        if instance is None:
            return super().__new__(cls)
        return instance

```

Then, after get the instance object memory pointer, the interpreter will call \_\_init__ method to initialize the instance. It takes the newly created instance (self) and additional arguments passed during instance creation.

_In fact, we usually re-write this function to realize specific personal demand._

```python
# default __init__ function
class DefClass(Object):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

# specific __init__ func
class Count:

    def __init__(self, num1: int = None, num2: int = None):
        self._num1 = num1
        self._num2 = num2
    
    def add(self):
        return self._num1 + self._num2

cont = Count(1, 2)
print(cont.add())
# the result: 3
```

_Attention: we should initiate the supclass when we re-write the `__init__` method._

After initiating the class instance, then the interpreter will re-write the instance's `__dict__` variable -- the static variable existed in every class.

_The difference between the class `__dict__` and the instance `__dict__`: When create the instance, this variable will be re-write and overrided. The class `dict` means the variables declared in class space, which the instance `dict` variables declared in `__init__` method._

```python
# the class __dict__ and instance __dict__

class Myclass:

    test_var = 'variable 1'

    def __init__(self):
        self._var = 'variable 2'

ins = Myclass()
print(Myclass.__dict__)
print(ins.__dict__) 

# the result:
# {'__module__': '__main__', 'test_var': 'variable 1', '__init__': <function Myclass.__init__ at 0x000001D8BA3396C0>, '__dict__': <attribute '__dict__' of 'Myclass' objects>, ...}
# {'_var': 'variable 2'}
```

-----

```python
    def bisect_left(a, x, lo=0, hi=None):
        """Return the index where to insert item x in list a, assuming a is sorted.

        The return value i is such that all e in a[:i] have e < x, and all e in
        a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
        insert just before the leftmost x already there.

        Optional args lo (default 0) and hi (default len(a)) bound the
        slice of a to be searched.
        """

        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo+hi)//2
            # Use __lt__ to match the logic in list.sort() and in heapq
            if a[mid] < x: lo = mid+1
            else: hi = mid
        return lo
```
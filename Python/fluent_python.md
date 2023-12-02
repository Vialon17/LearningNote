# Fluent Python

Here's my notes about the book [fluent python v1](https://hk1lib.org/book/3676951/3d1fce).  
-- vialon, Feb, 24, 2022

_Fluent Python v2(2021) is [here](https://hk1lib.org/book/17194890/bf297b), just have English version._

**Before Reading**

Let me explain the structure of this file.

It won't contain all points but some parts that I think is important in Fluent Python. I divide every chapter into three parts: the important point, the baisc konwlegde point and the summary.

-----

## 2: Data Structure

***Part - 1: Other Important Points***

### 2.8 [Bisect Module](https://docs.python.org/3/library/bisect.html)

__Order list:__

* `list.sort()` -> return None, __but has changed the list object itself!__
  
* `sorted(list)` -> return [Ordered NewList], never change the list but created a new list object.
  
* parameter(_Both_): list, reverse = false, key = (identity function)
  
* the difference:
  
  * The `list.sort()` function is a list build-in function;
  * `sorted()` function is a default function;
  * The return, the list itsele is changed or not; 
 

It's very useful to use this module to control the `ordered list`.

`bisect.bisect(haystack, needle, lo = 0, hi = len(a), *, key = None)`.

To find the `needle's position` in the haystack, the parameters 'lo' and 'hi' will determine the range of search(start with 'lo' and the search range is 'hi').

Use Bisect to search and sort the student's score.

```python
    import bisect
    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

    [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    # the result:
    # >>> ['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

### 2.9.2 MemoryView

Python will create a copy of the object in the memory which we are operating，but it'll spend lots of time to finish this work when there comes the float lists containning lots of members, but in fact we don't need create a mapping object so the MemoryView function will be very useful.

MemoryView will return an object without creating the copy object in memory and it'll reduce the memory cost and improve the running speed by using buffer protocol.

Syntax: `MemoryView(Obj) -> Obj`.

--------

***Part - 2: Basic Knowledge Points***

### Listcomps:
    
  __According to Python Cicada and in order to improve the code readablity, we create `list comprehension` and `generator expression` in python.__

  The purpose of Listcomps is just creating a list:
  ```python
  colors = ['black', 'white']
  sizes = ['S', 'M', 'L']
  tshirts = [(color, size) for color in colors for size in sizes]
  #>>> tshirts
  # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
  ```
  _You can also use `if...else...` syntax in it; It's a closure environment._

----

### Genexps:
    
  Different from Listcoms, Genexps show better in creating iterative list and combining with other list-container. It'll provide great help with the memory cost compared with its brother.  

  In form, Genexps just replace the '[]' with '()' based on Listcomps.

  ```python
  colors = ['black', 'white']
  sizes = ['S', 'M', 'L']
  for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): 
      print(tshirt)
  #printout -> :
  #>>> black S
  #>>> black M
  #>>> black L
  #>>> white S
  #>>> white M
  #>>> white L
  ```
  * __Function filter and map:__

    **Filter** function receivers two parameters and return an iterative object, it'll filter out the elements which couldn't go through the judge function: 

    &nbsp;&nbsp;&nbsp;**parameter** -> judge function, iterative object.
    &nbsp;&nbsp;&nbsp;**return** -> generator object.

    _u can use `list()` function to change the object into a list if u need a list._

    ```python
    a = [1, 2, 4, 'x', 'y', 5]
    b = filter(lambda c:isinstance(c, int), a)
    print(b)
    # >>> <filter object at 0x000001C7385B2F70>
    list(b)
    # >>> [1, 2, 4, 5]
    ```

    ***Map*** function also receivers several parameters and return an iterative object, it'll create a functional mapping among the parameters:

    &nbsp;&nbsp;&nbsp;**parameter** -> function/iterative object.
    &nbsp;&nbsp;&nbsp;**return** -> generator object.


    ```python
    def square(x):
        return x ** 2
    map(square, [1,2,3,4,5])
    # >>> <map object at 0x100d3d550>
    list(map(square, [1,2,3,4,5]))
    # >>> [1, 4, 9, 16, 25]
    ```

    __Comared__ with combination of filter and map, Listcomps seems like more pythonic.[^1]

    ```python
    >>> symbols = '$¢£¥€¤'
    >>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    >>> beyond_ascii
    [162, 163, 165, 8364, 164]
    >>> beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    >>> beyond_ascii
    [162, 163, 165, 8364, 164]
    ```
-----

### Tuple
 
__It's__ a mistake that just regard Tuple as stable List type, this pretty young thing will provide a container to store separate data and their location information.

**Different from List, Tuple is usually used to store mussy or no-named data while List always contains data with same type.**

* **Unpark Tuple**

  __We__ can combine the mussy data into several useful groups through Tuple Unpark or extract the useful data from tuple if there have some useless informations. 
  
  _In fact, the List type is also support with the unpark operation._

  ```python
  metro_areas = ('Tokyo','JP',36.933,(35.689722,139.691667))
  city, country, pop, location = metro_areas
  print(city, country, pop, location)
  # >>> Tokyo JP 36.933 (35.689722, 139.691667)
  # we just want the city and location
  city, *other, (_, latitude) = metro_areas
  print(city, other, latitude)
  # >>> Tokyo ['JP', 36.933] 139.691667
  ```

  __Yes__, it's a good idea using `_` _placeholder_ and `*` operator to deal with the remainder, but the operator `*` should appear just once time in a single code line. Seemingly we can also found it that the unpark operation can be used in nested tuple.

* **NamedTuple**

    __NamedTuple__ is a factory function, which creates a named-tuple template class and can be very useful in analyse data and debug code.

    __NameTuple__ inherits most property from Tuple 
    ```python
    from collections import namedtuple
    # It's packed in collections module
    city = namedtuple('city', 'name country population coordinates')
    Tokyo = city('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(Tokyo.country, Tokyo.population, Tokyo.coordinates)
    # >>> JP 36.933 (35.689722, 139.691667)
    print(Tokyo[1])
    # >>> JP
    ```
------

***Part - 3: The Summary***

### 2.11 Summary

_May it's suitable putting the important knowledge points here, I privately think._

#### The Function

* Container List: `list`, `tuple`, `collections.deque` (_store different types of data._)
  
* Flat List: `str`, `bytes`, `bytearray`, `memoryview`, `array.array` (_data must have same type._)

----

## Beautiful Python

This part is mainly about Pythonista(_python master_) Code.

Python, as the most hightest readablity language and its creation philosophy, can create popular and easy-to-understand code.

So we should follow the Python Zen:
```
# import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
...
```

_Recently, I had did some programs with my boss, and he did some code guideance to me, which made me realize the importance of code quality. So I had read the book -- [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/)_



----
## Decorators and Closures

### Decorator

**Decorator**, as one of the most successful [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern), has been used in many programming languages, as well as in Python. Decorator means that we can add some decorations for our specific functions, in anothe way -- **add some extra features to the function.**

In Python, we can regard the decorator as specific function which packages the target function, and use it as the syntax sugar `@` before the target function.

Let's have an instance.

```python
from time import time

# the decorator --> calculate the function run time
def timer(func):
    def inner_func(*args, **kwargs):
        print('here is the real function.')
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'the function {func.__name__} costs {end_time - start_time}s.')
        return result
    return inner_func


@timer
def test_func():
    x, res = 1, 0
    for i in range(100000):
        res = res + x * i
        x += 1
    return res

test_func()

# the console:
# >>> here is the real function.
# >>> the function test_func costs 0.005997180938720703s.
# >>> 333333333300001
```

The decorator can also add some parameters as normal function, but when doing this, we need package the decorator first, the function structure will be this:

> the decorator --- get the real decorator's parameters
>> the real decorator --- get the target function
>>> the inner function --- get the target function's parameters

```python
    import os, time

    def fatory_decorator(active = False):
        #get the decorator's parameters -> active
        def decorator(func):
            # the decorator is the real decorator of function
            print('here here')
            def clock(*arg, **kwargs):
                # the addition function of the decorator
                start_time = time.time()
                if active:
                    print(arg, kwargs)
                else:
                    print('active has closed.')
                func_return = func(*arg, *kwargs)
                run_time = time.time() - start_time
                return func_return, run_time
            return clock
        return decorator

    @fatory_decorator(active = True)
    def func1(arr: list, sleep_time = 5):
        time.sleep(sleep_time)
        print('Here start game.')
        temp_sum = 0
        for i in range(len(arr)):
            arr[i] = arr[i] + temp_sum
            temp_sum = arr[i]
        return arr

    temp_list = [1,2,3,4,5]
    arr, run_time = func1(temp_list, 6)
    print(f'the function {func1.__name__} get a list and return the list {arr} after running {round(run_time, 2)} seconds.')

    # >>> here here
    ### freeze 6s there
    # >>> Here start game.
    # >>> the function clock get a list and return the list [1, 3, 6, 10, 15] after running 6.01 seconds.
```
We can also find that the `class decorator` like in [Flask](https://flask.palletsprojects.com/en/3.0.x/):

```python
# creat a flask app
from flask import Flask, request, jsonify
from flask_cors import CORS

# enable CORS(cross-origin-resource-share) 
app = Flask(__name__)
CORS(app)

# specify index route to the server
@app.route('/', method = ['GET', 'POST'])
def index():
    return 'OK'

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8080, debug = True)
```

In this Flask instance, we can see there comes the class decoretor `app.route`, in fact, decorator can be created inside an object like this:

```python
# create a class decorator
# outter decorator

class Temp:
    num = 1
    cot = 0

    def count(func):
        def inner(*args, **kwargs):
            print(f'we have call the funcion count times.')
            return func(*args, **kwargs)
        return inner

@Temp.count
def test(num):
    print(num)

test(1)

# the resule:
# >>> we have call the funcion count times.
# >>> 1
```

But when we wanna call the class's attribute `cls.cot`, this function will raise error `TypeError: Temp.count() takes 1 positional argument but 2 were given`, so we should update our function:

```python
# inner class decorator
class Temp:
    num = 1
    cot = 0

    def inner_count(func):
        def inner(self, *args, **kwargs):
            print(f'we have call the funcion count times.')
            print(f'we get {self.cot} attribute.')
            return func(self, *args, **kwargs)
        return inner

    @inner_count
    def test(self, num):
        print(num)

Temp().test(1)
# the result:
# >>> we have call the funcion count times.
# >>> we get 0 attribute.
# >>> 1
```

There, there, here are the common decorators used in diary work. You can also read this article -- [Python Decorator](https://zhuanlan.zhihu.com/p/638893090)(zh_cn), it has similar demonstration. :)

------
[^1]: [The Zen of Python](https://peps.python.org/pep-0020/) -> Pythonic: Firstly, as a python engineer, we must walk like a python and this way is called pythonic 😗.
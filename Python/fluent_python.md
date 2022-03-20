# Fluent Python

Here's my notes about the book [fluent python v1](https://hk1lib.org/book/3676951/3d1fce).  
-- vialon, Feb, 24, 2022

_Fluent Python v2(2021) is [here](https://hk1lib.org/book/17194890/bf297b), just have English version._

**Before Reading**

Let me explain the structure of this file.

It won't contain all points but some parts that I think is important in Fluent Python. But I make a summary for every chapter in order to review in the future.

## 2:: Data Structure
### 2.8 [Bisect Module](https://docs.python.org/3/library/bisect.html)

__Order list:__
> * `list.sort()` -> return None, __but has changed the list object itself!__
> * `sorted(list)` -> return [Ordered NewList], never change the list but created a new list object.
> * parameter(_Both_): list, reverse = false, key = (identity function)
> * the difference:
>   * The `list.sort()` function is a list build-in function;
>   * `sorted()` function is a default function;
>   * The return, the list itsele is changed or not; 
> 

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

### 2.11 Summary

_May it's suitable putting the important knowledge points here, I privately think._

#### The Function

* Container List: `list`, `tuple`, `collections.deque` (_store different types of data._)
  
* Flat List: `str`, `bytes`, `bytearray`, `memoryview`, `array.array` (_data must have same type._)
  
* __Listcomps:__
    
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

* __Genexps:__
    
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
    __Function filter and map:__

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

    __Comared__ with combination of filter and map, Listcomps seems like more beautiful. 

    ```python
    >>> symbols = '$¢£¥€¤'
    >>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    >>> beyond_ascii
    [162, 163, 165, 8364, 164]
    >>> beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    >>> beyond_ascii
    [162, 163, 165, 8364, 164]
    ```

* **Tuple**
 
    __It's__ a mistake that just regard Tuple as stable List type, this pretty young thing will provide a container to store separate data and their location information.

    **Different from List, Tuple is usually used to store mussy or no-named data while List always contains data with same type.**

    * **Unpark Tuple**

        
        
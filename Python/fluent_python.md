# Fluent Python

Here's my notes about the book [fluent python]().  
-- vialon, Feb, 24, 2022

## 2: Data Structure
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
    
    ____
    ```python
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    #>>> tshirts
    # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
    ```
* __Genexps:__
    
    ```python

    ```
* 
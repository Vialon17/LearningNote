# Fluent Python

Here's my notes about the book [fluent python]().  
-- vialon, Feb, 24, 2022

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
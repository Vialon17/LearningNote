# The Note

The things an object carries around can also include functions. A function attached to an object is called a method. (Non-function things attached to an object, such as imag, are called attributes).

## The decorator

**Decorator** is usually used to extend the funciton temporarily, even can change the numbers of returner.

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
```
The output:
```
    >>> here here
    ### freeze 6s there
    >>> Here start game.
    >>> the function clock get a list and return the list [1, 3, 6, 10, 15] after running 6.01 seconds.
```
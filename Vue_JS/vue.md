# Vue JS

As a Python programmer, it's a good idea to start JavaScript & Front-End with Vue3.

### About Vue

Vue is one of the most popular front-end frameworks, as known as its fast and reconfigurable. 
In fact, in the popular list: React, JQuery, Vue & Angular, Vue maybe is the most one similar with Python [Flask](https://flask.palletsprojects.com/en/3.0.x/), they share same programming idea -- **Widget and Recombine**.

### About JS

As known as the Front-End Three Parts:

- HTML
- CSS
- JavaScript

JavaScript has been one popular programming language for almost over 20 years, due to its dynamic type compilation and Java like response speed, it's welcome for all programmers.

In 2009, with the release of NodeJS -- the cross-platform, open-source JavaScript runtime environment, JS could run in server back-end, which means that it has become the standard Universal language. If u wanna be a Full-Stack Engineer but learn less about program language, JS is the standard answer.

Let's play with JS:
```js
// import other variable from other file
import { data } from './data'

// defind constant variable, normal variable and temporary variable 
const original_data = data.final()
var name_list = original_data.name
let phone_numbers_list = original_data.phone_num

let all_data = {
    'num': 1,
    'str': '12345',
    'list': [1, 2, 3, 4]
    'dict': {
        'temp_val': 1,
        'temp_val2': 2,
    }
}

// defind function
function update_phone (phones) {
    for (let i in phones) {
        if (phones[i].length < 11 && phones[i].substring(-2, 0) === '12') {
            phone[i] = '123456789'
        }
    }
}

// defind a object
class Temp {

    // like python `__init__` method.
    constructor(name, gender, phone) {
        this.name = name
        this.gender = gender
        this.phone = phone
    }

    // normal function -- print
    print_sth () {
        console.log(`this is a normal function, and get name: ${this.name}.`)
    }

    // this class attribute
    get phone_num () {
        return this.phone
    }
}

```

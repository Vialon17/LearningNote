# Learning Route
------
Recently I found there seems like I had to complete many tasks at same time, so It's time to write down a plan to help with my work.

### The Past

* **Rainmeter**
* **Basic Python**
* **Basic Algorithm and Data Structure**
* **SQL**
* **Git**
* **Basic OS**
* **Hardware Knowledge**

### The Next
Short
* **SQL Summary**
* **Kaggle Courses**

Long
* **Couesera Class(Machine Learning)**
* **Probability Theory**
* **Fluent Python**

### The Long Period

* **Algorithm(exercise and AI)**
* **Kaggle Competition**
* **Machine Learning(Watermelon Book)**
  
Date: 2022 June,04


## GPT
It seems there might have been a slight misunderstanding in the transcription or interpretation of your last message regarding backpropagation. Let's clarify how changes in outputs relate to changes in inputs during the backpropagation process in neural networks, especially considering the function and its derivatives.

### Correcting the Concept

In the context of neural networks, particularly during backpropagation, we typically calculate the gradient of the loss function with respect to the inputs of a node (or layer). This calculation involves applying the chain rule to propagate gradients backward through the network.

Suppose you have a layer where \( z \) is the input to the activation function \( g \), and \( A = g(z) \) is the output of this activation function. If you are backpropagating an error, and \( \delta A \) (often denoted as \( \frac{\partial L}{\partial A} \)) is the gradient of the loss function \( L \) with respect to the output \( A \), the goal is to find \( \delta z \) (often denoted as \( \frac{\partial L}{\partial z} \)), which is the gradient of the loss with respect to the input \( z \).

### Correct Formula in Backpropagation

The correct relationship derived from the chain rule would be:
\[ \delta z = g'(z) \cdot \delta A \]

Where:
- \( \delta z \) (or \( \frac{\partial L}{\partial z} \)) is the gradient of the loss with respect to the input \( z \).
- \( g'(z) \) is the derivative of the activation function \( g \) evaluated at \( z \).
- \( \delta A \) (or \( \frac{\partial L}{\partial A} \)) is the gradient of the loss with respect to the output \( A \).

### Example Using Sigmoid Activation

Let's consider a sigmoid activation function \( g(z) = \frac{1}{1 + e^{-z}} \). If you are backpropagating an error:

1. **Derivative Calculation**:
   The derivative of the sigmoid function, \( g'(z) \), is \( g(z)(1 - g(z)) \). 

2. **Applying the Chain Rule**:
   If you've calculated \( \delta A \) during backpropagation from the next layer, and you want to find \( \delta z \) to propagate further back:
   \[ \delta z = g'(z) \cdot \delta A = g(z)(1 - g(z)) \cdot \delta A \]

This formula correctly propels the gradient through the layer, taking into account both the effect of the activation function's shape at \( z \) (through its derivative \( g'(z) \)) and how much the subsequent layers' computations are affected by changes in \( A \) (captured by \( \delta A \)).

### Summary

In neural network training, particularly during backpropagation, the described method is essential for updating the weights effectively. Each layer's output sensitivity to its input is crucial for understanding how errors should flow backwards and influence the weights. The computation \( \delta z = g'(z) \cdot \delta A \) captures this sensitivity and allows for efficient and accurate training of the network.
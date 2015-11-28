# Bite

Bite is an exploration into alternative application architectures. It's not a clear statement that any
program architecture or coding style is wrong, it just explores the alternatives. It explores this in
python, because it makes the changes more explicit. NodeJS already offers a runtime where some very
important improvements have been made and this could obscure the point the code is trying to make.

Applications have become a lot more _networked_ over the past decade: databases, REST services, online
API's, Amazon EC2. These operations add to the latency of an app or process. Sequential code execution
makes it difficult to achieve good performance for a single threaded app.

Other issues relate to how state becomes more difficult to manage in larger applications and the increase
in coupling between code elements for larger applications.

There are in fact **three** issues that Bite hopes to tackle:

1. Reduce the impact of latency from networking. _gevent_ is a great example 
2. Allow code to run synchronously or asynchronously through callbacks without code changes.
3. Attempt to fully decouple code chunks, which supports reusability and testability.

The metrics to evaluate if the architecture is viable (in this order):

1. 50%: is the code readable and is it less complex than a standard C program?
2. 25%: does it perform well and is it easier to reuse?
3. 25%: is it easier to test?

If the answer is _yes_ to two of these, then the plan is to propose the architecture to the wider community.



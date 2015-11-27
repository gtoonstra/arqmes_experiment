# Architecture messaging experiment

This is a repository to hold bits of code for research into alternative architectures
for general applications. 

## Objectives

The "hello world" applications in C and C++ are very procedural and demonstrate the simplest
use of the language. Things changed a whole lot in recent years as applications became much more networked
and the focus shifted towards optimizing CPU resources in the face of networks that are relatively slow. 
This gave rise to asynchronous callback routines, co-routines and other patterns that help to keep the CPU 
busy as best as possible in the face of many connected clients and services.

This project is about going a couple of steps further and investigate how typical batch applications written
in C, C++ and python could be changed to make them easier to understand, less complex and whether/if/how specific
architectures can help to keep particular concerns in code more contained. 

So what you'll find is not yet a determined solution towards those goals, but a range of experiments to gauge
if code remains readable, whether it makes sense to implement a "platform core" for applications, how to insert
particular concerns in easy way without having too large an impact on the general code base, etc.



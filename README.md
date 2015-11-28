# Bite

Bite is an exploration into alternative application architectures. Does this mean there's something wrong
wtih current architectures?

No. Millions of programs are written based on "textbook style" methods to write programs.

But... there may be other ways of structuring an(y) application which can bring additional benefits.
Applications have become a lot more _networked_ over the past decade: databases, REST services, online
API's, Amazon EC2. These operations add to the latency of an app or process. If it is built to process
things "sequentially", then any slowdown in this chain immediately impacts the latency of the entire
system.

There are in fact **three** issues that Bite hopes to tackle:

1. Reduce the impact of latency from networking. _gevent_ is a library that mostly resolves that.
2. Allow code to run synchronously or asynchronously through callbacks without code changes.
3. Attempt to fully decouple code chunks, which supports reusability and testability.

I'm pretty sure that all three things can be tackled in languages like NodeJS and Python, but attention
must be given how complex and readable that code remains. 

So the only metric used to evaluate the end result is code readability and program complexity. If it looks
easy enough to build applications with this new _architecture_, then let's propose it to the world out there
and see what they think.

## Background

The "hello world" applications in C and C++ are very procedural and sequential. Writing code that way works,
it's easy to understand, because all statements are logically ordered.

Unfortunately, there are some drawbacks:

1. State management (what the values are of variables when something is in a particular step of the process).
2. Coupling
3. Sequential programming paradigm

### State management

Variables are locations in memory that have a value or point to a data structure that manages some state. As applications
become larger and more "intricate" in the way how functions get used, this state management becomes more difficult
to manage. Especially in the case of multi-threaded code.

### Coupling

Coupling means how functions or pieces of code become dependent on one another. There are often specific libraries or
frameworks in use to build a particular application, so any application is "tied into" that particular framework and
it cannot always easily be refactored to use something totally different.

### Sequential programming paradigm

Applications tend to start out as sequential 'scripts' that call networked services in a specific order. The reason is that 
this is how we learn to program at school, a set of statements that manipulate a set of variables (state), which, when executed
in the particular order, achieves a certain objective.

It is clear though that GUI programming or "JavaScript browser code" follows different paradigms in the code and that it's no
longer fully sequential, but little pieces of code that react to user events and which manage a specific set of variables
available from somewhere: either married to the DOM or as a singleton variable.

Code that is asynchronous has the ability to get more work done, because it figures out which code 'chunk' can be worked on
to get ahead. This allows programmers to issue multiple requests at the same time and deal with the result of those requests
as they return **and** deal with UI logic and animations as they happen on user interaction. This is impossible to achieve
with purely sequential code.


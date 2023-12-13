# Bootstrap

Bootstrap is often described as a way to "build fast, responsive sites" and it is a "feature-packed, powerful, and extensible frontend toolkit". 

Some people refer to it as a "front-end" framework, and some are trying to be more specific by referring to it as a "CSS framework" or a “CSS library”. 

So, what is Bootstrap?

**Simply put, Bootstrap is a library of CSS and JavaScript code that you can combine to quickly build visually appealing websites.**

Modern web development is all about **components**. Small pieces of reusable code that allow you to build websites quickly. Bootstrap comes with multiple components for very fast construction of multiple components, or parts of components. 



Another important aspect of modern development is **responsive grids** which allow web pages to adapt their layout and content depending on the device in which they are viewed. Bootstrap comes with a pre-made set of CSS rules for building a responsive grid.

Bootstrap is very popular amongst developers as it saves development time and provides a way for developers to build visually appealing prototypes and websites.

![Screenshot 2023-11-20 at 2.32.10 PM](Notes/Screenshot%202023-11-20%20at%202.32.10%E2%80%AFPM.png)



![Screenshot 2023-11-20 at 2.33.40 PM](Notes/AlertBootStraps.png)

The main difference is hte color used in each alert. For example, the danger alert uses a red color whereas the primary alert uses a blue color. 

Bootstrap modifiers add a CSS class to change the visual style of components. You will use an infix to indicate the breakpoint in Bootstrap CSS rules.  



To build the responsive website. Use responsive grid and responsive library. Bootstraps uses Grid System to design a responsive webs seite. 



Bootstraps grid arrages things 

1. Containers
2. Rows
3. columns



## Static and Dynamic

What is the difference between Webserver and application server? 
**The application server generates the dynamic content that the web server sends back to the user’s browser.** 

It is slow to request dynamic servers. For that reason webservers have  caching. 

Cashing

* A saved copy of dynamic content readly available when request. 
* When the request is new, the webserver will cash the response for future  use.  Basically, when there is a reques, the webserver checks its cache to see if it has the response for that request. if it doesn't;t have the response then it requests the application server.  The webserver sends the dynamic response to the browser. For subsquent request, the webserver immediately sends the content stored in the cache. 



# Single Application Pages

It means one Html per whole webpage. 

## Bundling 

bundling will return all resources immediately 

## Lazy loading. 

lazy loading returns only the minimum required resources.



# React

Java script library. 

React allows developers to write less code to implement functionality in a web browser, it helps them maintain code in the long term and simplifies testing, and it also allows developers to re-use components when building their applications.

React uses a Virtual DOM to represent the browser DOM in memory.



# Python 

Data types

1. Numeric

2. Sequence

3. Dictionary

4. Boolean 

5. Set

   ![Screenshot 2023-11-29 at 10.25.21 AM](Notes/Screenshot%202023-11-29%20at%2010.25.21%E2%80%AFAM.png)

![Screenshot 2023-11-29 at 12.15.03 PM](Notes/Screenshot%202023-11-29%20at%2012.15.03%E2%80%AFPM.png)





# Procedure programming

* easy to learn
* Reusable
* Hard to maintain
* Code is exposed through out the progam 



### Alogarithms

Set of instructions to complete a task.

Key to solve the problem is to break the problem into small problem



# Functional Programming

Pure functions are used in functional programming to assure the integrity of data outside the scope of the pure function.     

Advantages of Pure functions

* Known outcome
* Consistent and reriable
* Cache : since you are know the out put each time
* Multi-threaded programs

Example

```python
my_list = [1,2,3]

def add_t_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_t_list(my_list, 10)
print(my_list) #[1, 2, 3]
print(new_list) # [1, 2, 3, 10]
```

Pure functions does not alter the global variables. 

* Pure functions keep the code cleaner and easy to debug.





# Recursion 

a function that calls itself

### Advantages

* Neat code
* Sub-problems
* Easy sequences

```python
def factorial (n):
    if n <= 1:
        return 1
    return n * factorial( n - 1)

print(factorial(0))
```

### Disadvantages

* Hard to follow

* Memory

* Debugging

  


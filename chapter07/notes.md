* Function decorators let us "enhance" the behavior of other functions.
* Decorators may change or totally replace the decorated function with a new one.
* Decorators ar executed immediately when a module is loaded.
* Decorator functions are usually written in a separate module than the _decorated_ functions.

### Variable Scope Rules
---
* Any variable assigned in the body of a function in Python is considered local (even if there was a global assignment done before the function). If we do want to enforce the variable in the function to be global, then we need to explicitly declare it so `global myVar`.

### Closures
---
* 
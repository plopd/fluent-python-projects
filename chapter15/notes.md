The else beyond if
---
Can be used in for, try, and while constructs:
    * for: else will execute only after succesfull completion of for (i.e., not after a break statement)
    * while: only if the while exits because of a falsy condition
    * try: if no exception is raised in the try block.

* To be clear and concise, add only statemens in a try block that may cause the exceptions to be raised. It makes it easier to read which code is guarded against possible errors and which is not. Equally, it becomes obvious that the code outside, following the try block will get called only if no exceptions are raised in the try block.

* try/except is commonly used for control flow, besides error handling. The mantra is EAFP as in "Easier to ask for forgiveness than permission".


Context managers and with blocks
---

* with blocks don't define a new scope, like functions or methods do, so you can still access objects inside the with after exiting them.
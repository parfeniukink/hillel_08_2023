Write a context manager that **measures** and **logs** the execution time of a code block inside it. Use the `time` module for timing and the `logging` module for logging. Test it with different pieces of code.

```python
import time
import logging

class TimerContext:
    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_value, traceback):
        # logger.info(...)
        ...

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with TimerContext():
    time.sleep(2)
```

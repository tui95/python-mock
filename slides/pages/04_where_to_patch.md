---
layout: section
---

# Where to patch


---
hideInToc: true
layout: center
---

## `patch("path.to.object")`

---
hideInToc: true
---

# How to know where to patch
1. How is it imported?
2. Where is it used?

---

## Individual import

<div class="grid grid-cols-2 gap-x-4 pt-4">

```python
# magic.py
import random

def get_magic_number() -> int:
    return random.randint(1, 100)
```

<div>

```python {all|3,9|all}
# main.py
import string
from magic import get_magic_number

def get_magic_char() -> str:
    chars = (
        string.ascii_letters + string.punctuation
    )
    magic_number = get_magic_number()
    return chars[magic_number % len(chars)]
```

</div>

</div>

<v-click>

```python {all|6|all}
# test_main.py
from unittest import mock
from main import get_magic_char

def test_get_magic_char() -> None:
    with mock.patch("main.get_magic_number", return_value=2):
        actual = get_magic_char()
        expected = "c"
        assert actual == expected
```

</v-click>

---

## Module import

<div class="grid grid-cols-2 gap-x-4 pt-4">

```python
# magic.py
import random

def get_magic_number() -> int:
    return random.randint(1, 100)
```

<div>

```python {all|3,9|all}
# main.py
import string
import magic

def get_magic_char() -> str:
    chars = (
        string.ascii_letters + string.punctuation
    )
    magic_number = magic.get_magic_number()
    return chars[magic_number % len(chars)]
```

</div>

</div>

<v-click>

```python {all|6|all}
# test_main.py
from unittest import mock
from main import get_magic_char

def test_get_magic_char() -> None:
    with mock.patch("magic.get_magic_number", return_value=2):
        actual = get_magic_char()
        expected = "c"
        assert actual == expected
```

</v-click>

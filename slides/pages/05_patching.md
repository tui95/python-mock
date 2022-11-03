---
layout: section
---

# Patching

---
hideInToc: true
---

# `unittest.mock.patch`

<div class="grid grid-cols-2 gap-x-4">

<div>

## `patch()`
```python
patch("path.to.object.attribute")
```

<v-click>

- builtins
- no need to import module

</v-click>

</div>

<div>

## `patch.object()`
```python
patch.object(path.to.object, "attribute")
```

<v-click>

- requires importing module to patch first
- make refactoring easier

</v-click>

</div>

</div>

---
hideInToc: true
---

# Patch scope
1. context manager
2. function decorator
3. class decorator
4. inline (need to manually call method to start and stop the mocking)

---
hideInToc: true
---

### 1. Context manager
```python
with patch.object(some_module, "some_function") as mock_some_function:
    ...
```

<v-click>

### 2. Function decorator

```python
@patch.object(some_module, "some_function")
@patch.object(some_module, "another_function")
def test_foo(another_function: mock.MagicMock, some_function: mock.MagicMock) -> None:
    ...
```

</v-click>

<v-click>

### 3. Class decorator

```python
@patch.object(some_module, "some_function")
class TestCase:
    def test_foo(some_function: mock.MagicMock) -> None:
        ...

    def test_bar(some_function: mock.MagicMock) -> None:
        ...
```

</v-click>

---
hideInToc: true
---

### 4. Inline (need to manually call method to start and stop the mocking)

<div class="pt-4">

#### `pytest`
```python
def test_foo(request: pytest.FixtureRequest) -> None:
    patcher = patch.object(some_module, "some_function")
    patcher.start()
    request.addfinalizer(patcher.stop)
    ...
```

<v-click>

#### `unittest`
```python
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        patcher = patch.object(some_module, "some_function")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_foo(self) -> None:
        ...
```

</v-click>

</div>

---
hideInToc: true
---

## `pytest-mock`

```python {all|7,8|all}
# test_main.py
from unittest import mock
from pytest_mock import MockerFixture
import magic
from main import get_magic_char

def test_get_magic_char(mocker: MockerFixture) -> str:
    mocker.patch.object(magic, "get_magic_number", return_value=2)
    actual = get_magic_char()
    expected = "c"
    assert actual == expected
```

---
hideInToc: true
---

# kwargs

1. `return_value`

2. `side_effect`

3. `new`

---
hideInToc: true
---

# `return_value`

<div class="grid grid-cols-2 gap-x-4 pt-4">

```python
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

```python
# magic.py
import random

def get_magic_number() -> int:
    return random.randint(1, 100)
```

</div>

<v-click>

```python {all|7|all}
# test_main.py
from unittest import mock
import magic
from main import get_magic_char

def test_get_magic_char() -> str:
    with mock.patch.object(magic, "get_magic_number", return_value=2):
        actual = get_magic_char()
        expected = "c"
        assert actual == expected
```

</v-click>

---
hideInToc: true
---

# `side_effect`

dynamic return value

1. Callable
2. Exception
3. Iterable

---
hideInToc: true
---

# `side_effect`: Callable

<div class="grid gap-y-4">

```python {all|3,8|all}
# main.py
from decimal import Decimal
import db

def get_book_prices(book_names: list[str]) -> dict[str, Decimal]:
    price_map = {}
    for name in book_names:
        book = db.get_book_by_name(book_name)
        price = book.price if book else None
        price_map[name] = date_published
    return price_map
```

```python
# db.py
def get_book_by_name(name: str) -> Optional[Book]:
    return Book.objects.filter(name=name).first()
```

</div>

---
hideInToc: true
---

# `side_effect`: Callable (continue)


```python {all|7-11|all}
# test_main.py
from unittest import mock
import db
from main import get_book_prices

def test_get_book_prices() -> None:
    name_to_book = {"Foo": Book(price=10)}
    def side_effect(book_name):
        return name_to_book.get(book_name)

    with mock.patch.object(db, "get_book_by_name", side_effect=side_effect):
        actual = get_book_prices(["Foo", "Bar"])
        expected = {
            "Foo": 10,
            "Bar": None,
        }
        assert actual == expected
```

---
hideInToc: true
---

# `side_effect`: Exception

```python
# main.py
import openpyxl
from openpyxl.utils.exceptions import InvalidFileException
from rest_framework import serializers

def load_workbook(filename: str) -> openpyxl.Workbook:
    try:
        return openpyxl.load_workbook(filename)
    except InvalidFileException:
        raise serializers.ValidationError("Failed to read an excel file")
```

<v-click>

```python {all|8|all}
import pytest
import openpyxl
from openpyxl.utils.exceptions import InvalidFileException
from rest_framework import serializers
from main import load_workbook

def test_load_workbook_with_invalid_file(mocker) -> None
    mocker.patch.object(openpyxl, "load_workbook", side_effect=InvalidFileException)
    with pytest.raises(serializers.ValidationError) as exc_info:
        load_workbook("foo.xlsx")
    expected_error_msg = "Failed to read an excel file"
    actual_error_msg, = exc_info.value.args
    assert actual_error_msg == expected_error_msg

```

</v-click>

---
hideInToc: true
---

# `side_effect`: Iterable

<div class="grid gap-y-4">

```python {all|7|all}
# main.py
def get_magic_text(length: int) -> str:
    lookup_chars = string.ascii_letters + string.punctuation
    lookup_chars_len = len(lookup_chars)
    chars = []
    for _ in range(length):
        magic_num = magic.get_magic_number()
        chars.append(lookup_chars[magic_num % lookup_chars_len])
    return "".join(chars)
```

<v-click>

```python {all|3|all}
# test_main.py
def test_get_magic_text() -> None
    with mock.patch.object(magic, "get_magic_number", side_effect=[2, 0]):
        actual = get_magic_text(2)
        expected = "ca"
        assert actual == expected
```

</v-click>

</div>

---
hideInToc: true
---

# `new`

patch attribute

<div class="grid grid-cols-2 gap-x-4">

```python {all|2,6|all}
# utils.py
import constants

def generate_apps_markdown_entry() -> str:
    entries = ["Apps\n"]
    for app in constants.APPS:
        entries.append(f"- {app}\n")
    return "".join(entries)
```

```python
# constants.py
APPS = [
    "core",
    "master_data",
    "site_settings",
    "drawing",
    "visualization",
    "planning",
    "evaluation",
    "summary",
    "note",
    "management",
    "users",
    "tracking",
    "issues",
]
```

</div>

---
hideInToc: true
---
# `new` (continue)

```python {all|2,15|all}
import textwrap
import constants
from utils import generate_apps_markdown_entry

def test_generate_apps_markdown_entry() -> None:
    # \ to start with the string and avoid the first newline
    expected = textwrap.dedent(
        """\
        Apps
        - foo
        - bar
        """
    )

    with mock.patch.object(constants, "A", new=["foo", "bar"]):
        actual = generate_apps_markdown_entry()
        assert actual == expected
```

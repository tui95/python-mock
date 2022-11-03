---
layout: section
---

# Speccing

---
hideInToc: true
---

# Pitfalls of mock

### Performing the followings on mock object will not result in an error

1. access non existing attributes or calling non existing methods
2. attemp to set non existing attributes
3. calling methods or functions with wrong/missing arguments


---
hideInToc: true
---

# `spec`
raise an error when accessing non existing attributes/methods

### `Mock` or `MagicMock`
```python
from restframework.request import Request

mock_request = mock.MagicMock(spec=Request)
```

<v-click>

### `patch()` or `patch.object()`
```python

with mock.patch("some_module.Request", spec=True):
    ...
```

</v-click>

---
hideInToc: true
---

# `spec_set`
raise an error when accessing non existing attributes/methods or setting non existing attributes

### `Mock` or `MagicMock`
```python
from restframework.request import Request

mock_request = mock.MagicMock(spec_set=Request)
```

<v-click>

### `patch()` or `patch.object()`
```python

with mock.patch("some_module.Request", spec_set=True):
    ...
```

</v-click>

---
hideInToc: true
---

# `autospec`
like `spec` but also raise an error when accessing attribute of attribute or using invalid method arguments

### `Mock` or `MagicMock`
```python
from restframework.request import Request

mock_request = mock.create_autospec(Request)
```

<v-click>

### `patch()` or `patch.object()`
```python

with mock.patch("some_module.Request", autospec=True):
    ...
```

</v-click>

---
hideInToc: true
---

# `spec` and `autospec` limitations

- Do not know about dynamic attributes (attributes set via constructors also count as dynamic)
- `autospec` has to access attributes of the real object and may trigger some code execution


For more details, read the official [Autospeccing docs](https://docs.python.org/3/library/unittest.mock.html#autospeccing)

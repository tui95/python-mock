---
layout: section
---

# Mock class

---
hideInToc: true
---

# Mock class

<v-click>

- create new attribute on the fly when they are accessed

```python
mock = Mock()
mock.filter(name="foo").order_by("-price")
```

</v-click>

<v-click>

- record how it is called

```python
>>> mock.mock_calls
[call.filter(name='foo'), call.filter().order_by('-price')]
```

</v-click>

<v-click>

- assert how it is called

```python
mock.filter.assert_called_once_with(name="foo")
mock.filter.return_value.order_by.assert_called_once_with("-price")
```

</v-click>

---
hideInToc: true
---

# `Mock` vs `MagicMock`

<div class="grid grid-cols-2 gap-x-4">

<v-click>

<div>

## `Mock`
- Can set `return_value`
- Can set `side_effect`
- Has `assert_*` methods

</div>

</v-click>


<v-click>

<div>

## `MagicMock`
- subclass of `Mock`
- implemented some magic methods such as
    - `__len__()`
    - `__bool__()`
    - etc...

</div>

</v-click>

</div>



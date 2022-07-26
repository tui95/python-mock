---
layout: section
---

# What is mocking?

---
hideInToc: true
---

## A type of test double

<div class="flex justify-center items-center h-full">

```mermaid {scale: 2.0}
flowchart LR
  sut[System Under Test] -.-> real(Real)
  sut --> td(Mock)
  style real stroke-dasharray: 4 4
```

</div>

---
layout: quote
hideInToc: true
---

# Definition

"Mocks are pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting."

<div class="text-right">
Martin Fowler
</div>

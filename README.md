# Life Game

This is  a class for lifegame based on python, and the generation is available if you has define the initial state with numpy.

for example, you have define a initial state:

```
import numpy as np
ground=np.random.random((10,10))>=0.5
ground.astype(int)
```

```
array([[0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
       [1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
       [1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
       [1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
       [0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
       [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]])
```

Creating the Instance

```
from lifegame import lifegame
lg=lifegame(ground.astype(np.int))
```

Index: generating after *n* times

```
#n=9
#lg[9]
array([[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
```

Slice: a series generating result

```
#lg[3:5]
[array([[0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 0]]),
 array([[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0]])]
```

For loop

```
count = 0
for im in lg:
    print(im)
    count += 1
    if count == 5:
        break
```

```
[[0 0 1 1 1 0 1 0 0 1]
 [1 0 1 1 1 1 1 0 0 0]
 [0 1 0 0 1 1 0 0 1 1]
 [1 1 1 0 0 1 0 1 1 1]
 [1 1 1 1 1 1 1 0 1 0]
 [0 1 0 0 0 1 1 0 1 1]
 [0 1 0 1 1 0 1 1 0 0]
 [0 0 0 1 0 1 0 1 1 1]
 [0 1 1 0 1 1 0 0 1 0]
 [1 0 0 1 1 1 1 1 1 0]]
[[0 1 1 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 1]
 [0 0 0 1 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 1]
 [0 1 1 0 0 0 0 0 0 0]
 [0 1 1 1 0 0 1 1 1 0]]
[[0 1 1 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 0 0 0 1]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 1]
 [0 0 0 1 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0 0 1]
 [0 1 1 0 0 0 0 0 0 0]
 [0 1 1 1 0 0 1 1 1 0]]
[[0 0 0 0 0 0 1 0 1 0]
 [0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 1]
 [0 1 0 0 0 0 0 0 0 0]
 [1 0 0 1 0 0 0 1 1 0]
 [0 1 0 1 0 0 0 1 0 0]]
[[0 0 0 0 0 0 1 0 1 0]
 [0 0 0 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 0 1 0 1]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 1 1]
 [0 1 0 0 0 0 0 0 0 0]
 [1 0 0 1 0 0 0 1 1 0]
 [0 1 0 1 0 0 0 1 0 0]]
```


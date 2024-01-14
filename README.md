Credit to mtrmk for pointing out to me that the print statement for the for loop for finding rando garbage characters should be a separate line underneath the line where python randomly selects garbage characters the first time. This is an improvement because python would have run the randomization again for the print statement and I would have gotten different characters. He also pointed out to me a for loop 

```py
for i in range(garbage_placement):
    garbage_char = random.choice(garbage_chars)
    print(garbage_char, end="")
    garbage_row.append(garbage_char)
```

mtrtmk helped me figure out how to write scalable code for determining the len of the string. 

```py

garbage_row = ['0x2678', '?', '(', ')', '<', 'VWXYZZZ']

# Total Length = (Len of hex string) + (Number of garbage chars) + (Len of keyword)
length = len(garbage_row[0]) + len(garbage_row[1:-1]) + len(garbage_row[-1])
print(length)
# 17

# OR
length = 0
for element in garbage_row:
    length += len(element)
    
print(length)
# 17
```

this scalable mtrmk helped me come up with helps me determine the length of the game row so that I can implement different game row sizes should I wish to implement an intermediate or hard mode.
```py
# I chose _ as loop variable because it isn't being used in the loop body.
# If you wish, you can use i or j as the loop variable.
# limit is how long your final string is supposed to be. 
# If you want a 16 char string, then you should use 16 in place of limit.
# For length, see the earlier example.

for _ in range(limit - length):  
    garbage_char = random.choice(garbage_chars)
    garbage_row.append(garbage_char)
```

## Writeup for FakeItt - Pwn:
- Input following string and you get the flag:
```
aaaaaaaaaaaaaaa%20$hhn
```

This **format string vulnerability** writes the value 0xf (15 in hex) to 20th stack and theres a pointer to character.
Basically skipping ./fake_ 
And just making it read from flag.txt
Expressions speak louder than words.

Flag format: `nca{...}`

**Challange Files**: [message.txt](message.txt)

---

## Solution & Writeup
- Use regex:
```bash
cat message.txt | grep -oP 'nca\{[a-zA-Z0-9_]+\}'
```
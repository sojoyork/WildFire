# WildFire
It is a REALLY fast password cracker made with python! It is made for pentests whre you get a probably simalar hash that is a weak password hash that is common so what you do? CRACK IT USING WILDFIRE! Here is how it works
| pass.txt | How WildFire sees it as | hash.txt | They match?
| --- | ----------- |-----------------------|-----------------------------------|
| hello | 5d41402abc4b2a76b9719d911017c592 | 5d41402abc4b2a76b9719d911017c592  | True
| bye | bfa99df33b137bc8fb5f5407d7e58da8 |  bfa99df33b137bc8fb5f5407d7e58da8 | True
| grass | 09d440e487d45777c05c3a6552ad9154 | 05b8c74cbd96fbf2de4c1a352702fbf4 | False

The output will be this:
```zsh
yeetic@DESKTOP-BJ6KRG9:~/wildfire$ python3 wildfire.py hashes.txt wordlist.txt --hash-format md5
[!] Cracking...
[+] Done!
=========================
wordlist: wordlist.txt
hash file: hashes.txt
=========================
[+] Password: hello
[+] Password: bye
```

It does not show the password that was failed to get decrypted

## How do i install it?
Install the installer by installing <a href="install.py" download>Installer</a>

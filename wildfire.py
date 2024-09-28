import hashlib
import argparse
import crypt

def hash_word(word, hash_format):
    if hash_format == 'md5':
        return hashlib.md5(word.encode()).hexdigest()
    elif hash_format == 'sha1':
        return hashlib.sha1(word.encode()).hexdigest()
    elif hash_format == 'sha256':
        return hashlib.sha256(word.encode()).hexdigest()
    elif hash_format == 'crypt':
        return crypt.crypt(word, crypt.mksalt(crypt.METHOD_SHA256))  # You can specify other methods too
    else:
        raise ValueError(f"Unsupported hash format: {hash_format}")

def wildfire(password_hashes, wordlist, hash_format='md5'):
    found_passwords = {}

    for word in wordlist:
        hashed_word = hash_word(word.strip(), hash_format)
        if hashed_word in password_hashes:
            found_passwords[word.strip()] = hashed_word

    return found_passwords

def load_password_hashes(file_path):
    with open(file_path, 'r') as file:
        return {line.strip() for line in file}

def main():
    parser = argparse.ArgumentParser(description='Password Cracker Tool (Wildfire)')
    parser.add_argument('hash_file', help='File containing password hashes (one per line)')
    parser.add_argument('wordlist_file', help='File containing the wordlist (one word per line)')
    parser.add_argument('--hash-format', choices=['md5', 'sha1', 'sha256', 'crypt'], default='md5',
                        help='Specify the hash format (default: md5)')

    args = parser.parse_args()

    # Load password hashes from the provided file
    password_hashes = load_password_hashes(args.hash_file)

    # Load the wordlist
    with open(args.wordlist_file, 'r') as file:
        wordlist = file.readlines()

    # Output initial cracking message
    print("[!] Cracking...")

    # Run the wildfire cracker
    cracked_passwords = wildfire(password_hashes, wordlist, args.hash_format)

    # Output completion message
    print("[+] Done!")
    print("=========================")
    print(f"wordlist: {args.wordlist_file}")
    print(f"hash file: {args.hash_file}")
    print("=========================")

    # Display results
    if cracked_passwords:
        for password, hashed in cracked_passwords.items():
            print(f"[+] Password: {password}")
    else:
        print("No passwords were cracked.")

if __name__ == "__main__":
    main()

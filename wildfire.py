import hashlib
import itertools
import string
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

# List of supported hash functions
SUPPORTED_HASHES = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512
}

def hash_string(s, hash_type):
    """Calculate hash of the string using the specified hash type"""
    hash_func = SUPPORTED_HASHES.get(hash_type)
    if not hash_func:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    return hash_func(s.encode()).hexdigest()

def find_hash_match(target_hash, hash_type, length, start, end):
    """Find a matching hash within a given range of characters."""
    chars = string.ascii_lowercase
    for combination in itertools.islice(itertools.product(chars, repeat=length), start, end):
        candidate = ''.join(combination)
        if hash_string(candidate, hash_type) == target_hash:
            return candidate
    return None

def worker(task_queue, result_queue, target_hash, hash_type, length):
    """Worker function for multithreading to find hash matches."""
    while not task_queue.empty():
        try:
            start, end = task_queue.get_nowait()
            match = find_hash_match(target_hash, hash_type, length, start, end)
            if match:
                result_queue.put(match)
                return
        except queue.Empty:
            return

def parallel_brute_force(target_hash, hash_type, length, num_threads):
    """Use multithreading to brute-force find a matching hash."""
    chars = string.ascii_lowercase
    total_combinations = len(chars) ** length
    chunk_size = total_combinations // num_threads

    task_queue = queue.Queue()
    result_queue = queue.Queue()

    # Creating tasks for each thread
    for i in range(0, total_combinations, chunk_size):
        task_queue.put((i, min(i + chunk_size, total_combinations)))

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(task_queue, result_queue, target_hash, hash_type, length))
        threads.append(t)
        t.start()

    # We also use threads to manage multiple processing tasks
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(t.join) for t in threads]
        for future in futures:
            future.result()  # Wait for each thread to complete

    # Check if a match was found
    if not result_queue.empty():
        return result_queue.get()
    return None

if __name__ == "__main__":
    # Example usage:
    target_hash = "5d41402abc4b2a76b9719d911017c592"  # Example for "hello" with MD5
    hash_type = "md5"
    length = 5  # Length of the word we're trying to find
    num_threads = 4  # Number of threads to use

    # This will run the brute-force attack
    result = parallel_brute_force(target_hash, hash_type, length, num_threads)
    if result:
        print(f"Match found: {result}")
    else:
        print("No match found.")

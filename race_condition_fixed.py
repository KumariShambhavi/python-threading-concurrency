"""
Race condition fix: Use threading.Lock to synchronize file writing.
"""
import threading
import time

lock = threading.Lock()

def write_to_file(filename: str, text: str) -> None:
    """Append text to a file safely with Lock."""
    with lock:
        with open(filename, "a") as f:
            f.write(text + "\n")

def main() -> None:
    threads: list[threading.Thread] = []
    start = time.time()

    for i in range(10):
        t = threading.Thread(target=write_to_file, args=("race_output_fixed.txt", f"Thread-{i}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"File writing (with Lock) took {end - start:.2f} seconds. Check race_output_fixed.txt for correctness.")

if __name__ == "__main__":
    main()

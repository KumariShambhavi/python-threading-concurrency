"""
Race condition demo: Multiple threads writing to the same file without Lock.
"""
import threading
import time

def write_to_file(filename: str, text: str) -> None:
    """Append text to a file (race condition possible)."""
    with open(filename, "a") as f:
        f.write(text + "\n")

def main() -> None:
    threads: list[threading.Thread] = []
    start = time.time()

    for i in range(10):
        t = threading.Thread(target=write_to_file, args=("race_output.txt", f"Thread-{i}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"File writing (without Lock) took {end - start:.2f} seconds. Check race_output.txt for corruption.")

if __name__ == "__main__":
    main()

# Python Threading and Concurrency

## Objective
This report explores Python's `threading` module, the Global Interpreter Lock (GIL), and concurrency tools such as `Lock`, `Queue`, and `ThreadPoolExecutor`. It also applies these concepts to two practical tasks:
1. An image downloader (single-threaded vs. threaded).
2. A race condition demo (with and without Lock).

---

## Topics Studied

### 1. Threading Module & GIL Limits
- The `threading` module allows concurrent execution of tasks by running multiple threads within the same process.
- **Global Interpreter Lock (GIL):**
  - Ensures only one thread executes Python bytecode at a time.
  - Limits true parallelism for CPU-bound tasks.
  - **Good fit:** I/O-bound tasks (network requests, file I/O).
  - **Poor fit:** CPU-intensive computations (better handled by `multiprocessing`).

**Sources:**  
- [Python Docs: threading](https://docs.python.org/3/library/threading.html)  
- Real Python articles on threading & concurrency.  

---

### 2. Locks
- Threads writing to shared resources (e.g., files, counters) may cause **race conditions**.
- `threading.Lock` ensures only one thread modifies a resource at a time.
- Tradeoff: Serialization (slight slowdown) in exchange for correctness.

---

### 3. Queue
- `queue.Queue` provides **thread-safe data sharing** between producer and consumer threads.
- Automatically handles locking internally.

---

### 4. ThreadPoolExecutor
- Part of `concurrent.futures`.
- Simplifies thread management by handling creation, scheduling, and destruction of worker threads.
- Useful for parallelizing I/O-heavy workloads without managing raw `threading.Thread` objects.

---

## Tasks

### Task 1: Image Downloader
- **Single-threaded version:** Downloads 20 images sequentially.
- **Threaded version:** Spawns 20 threads, each downloading one image concurrently.
- Expectation: Threaded version should be significantly faster due to concurrent network I/O.

---

### Task 2: Race Condition Demo
- **Without Lock:** Multiple threads append to the same file, leading to interleaved and corrupted output.
- **With Lock:** `threading.Lock` ensures each thread writes atomically, producing correct output.

---

## Timing Results

| Task                     | Without Threads / Lock | With Threads / Lock |
|---------------------------|-------------------------|----------------------|
| Task 1: Image Downloading | X.XX sec               | Y.YY sec             |
| Task 2: File Writing      | A.AA sec (corrupt data) | B.BB sec (correct data) |

*(Replace `X.XX`, `Y.YY`, etc. with actual timing after running code.)*

---

## Key Learnings & Conclusions
- Python's GIL restricts true parallelism but **threading excels in I/O-bound tasks**.
- Locks are essential to prevent race conditions but may slightly reduce throughput.
- `Queue` and `ThreadPoolExecutor` provide safer and more maintainable abstractions over raw threading.
- Correctness often outweighs raw speed when handling shared resources.

---

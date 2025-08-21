# Python Threading and Concurrency 🚀

## Overview
This project demonstrates **Python threading and concurrency concepts** with practical tasks.  
It explores:
- The **threading module** and the impact of the **Global Interpreter Lock (GIL)**
- Using **Locks** to prevent race conditions
- Safe communication with **Queues**
- Managing workers using **ThreadPoolExecutor**

Two main tasks are implemented:
1. **Image Downloader** – Compare single-threaded vs. multi-threaded execution.
2. **Race Condition Demo** – Show race conditions in file writing and fix them using `Lock`.

---

## Features
- 📥 Download images using 20 threads vs. a sequential approach  
- ⚡ Performance comparison of threaded vs. non-threaded execution  
- 📝 Demonstration of **race condition issues** in file writing  
- 🔒 Fix for race conditions using **threading.Lock**  
- 📊 Timing table to measure performance differences  

---

## Project Structure
python-threading-concurrency/
│
├── image_downloader_single.py # Single-threaded image downloader
├── image_downloader_threaded.py # Threaded image downloader
├── race_condition_demo.py # Race condition demo without Lock
├── race_condition_fixed.py # Fixed race condition with Lock
├── Threading_and_Concurrency_Documentation.md # Full detailed documentation
└── README.md # Project overview (this file)


---

## Getting Started

### Prerequisites
- Python 3.10+ recommended
- Required libraries:  
  
  pip install requests
Running the Scripts
Single-threaded Image Downloader:


python image_downloader_single.py
Multi-threaded Image Downloader:


python image_downloader_threaded.py
Race Condition Demo (without Lock):


python race_condition_demo.py
Race Condition Fixed (with Lock):


python race_condition_fixed.py
Example Output

Single-threaded download time: 15.34 seconds
Threaded download time: 4.87 seconds

File writing (without Lock) took 0.02 seconds. Check race_output.txt for corruption.
File writing (with Lock) took 0.03 seconds. Check race_output_fixed.txt for correctness

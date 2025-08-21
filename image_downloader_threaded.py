"""
Multi-threaded image downloader using threading.
Spawns 20 threads to download images concurrently.
"""
import time
import requests
import threading

def download_image(url: str, filename: str) -> None:
    """Download an image from a given URL and save it to disk."""
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

def main() -> None:
    urls = [f"https://picsum.photos/200?random={i}" for i in range(20)]

    threads: list[threading.Thread] = []
    start = time.time()

    for i, url in enumerate(urls):
        t = threading.Thread(target=download_image, args=(url, f"image_threaded_{i}.jpg"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f"Threaded download time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()

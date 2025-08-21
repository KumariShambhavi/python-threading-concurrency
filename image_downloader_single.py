"""
Single-threaded image downloader.
Downloads images sequentially from a list of URLs.
"""
import time
import requests

def download_image(url: str, filename: str) -> None:
    """Download an image from a given URL and save it to disk."""
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

def main() -> None:
    urls = [f"https://picsum.photos/200?random={i}" for i in range(20)]

    start = time.time()
    for i, url in enumerate(urls):
        download_image(url, f"image_single_{i}.jpg")
    end = time.time()

    print(f"Single-threaded download time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()

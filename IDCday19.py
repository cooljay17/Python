# Download multiple files concurrently using threads
import threading
import requests

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {url} to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_files_threaded(files):
    threads = []
    for url, file_path in files:
        thread = threading.Thread(target=download_file, args=(url, file_path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete

if __name__ == "__main__":
    files_to_download = [
        ("https://github.com/cooljay17/Sample_Files/blob/main/r1.jpeg", "r1.jpeg"),
        ("https://github.com/cooljay17/Sample_Files/blob/main/r2.jpeg", "r2.jpeg"),
        ("https://github.com/cooljay17/Sample_Files/blob/main/r3.jpeg", "r3.jpeg"),
    ]
    download_files_threaded(files_to_download)

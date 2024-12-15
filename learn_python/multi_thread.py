import threading
import time

def download_file(file_name, download_time):
    print(f"Starting to download {file_name}...")
    time.sleep(download_time)
    print(f"Downloaded {file_name} in {download_time} seconds.")

def process_data(data):
    print(f"Starting to process data: {data}...")
    time.sleep(2)
    print(f"Finished processing {data}.")

def main():
    download_thread = threading.Thread(
        target=download_file, args=('File1.txt', 5))
    process_thread = threading.Thread(target=process_data, args=('DataSet1',))
    download_thread.start()  # Starts the download operation in a new thread.
    process_thread.start()
    download_thread.join()  # Waits for the download thread to finish.
    process_thread.join()   # Waits for the processing thread to finish.
    print("Both tasks are completed.")


if __name__ == "__main__":
    main()

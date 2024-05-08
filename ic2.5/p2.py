import shutil
import threading

source_files = ['./file0', './file1', './file2']
dest_directory = './projects'

def copy_file(num):
    shutil.copy(source_files[num], dest_directory)
    print(f"Copied {source_files[num]}")


threads = []
for num in range(len(source_files)):
    thread = threading.Thread(target=copy_file, args=(num,))
    threads.append(thread)


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


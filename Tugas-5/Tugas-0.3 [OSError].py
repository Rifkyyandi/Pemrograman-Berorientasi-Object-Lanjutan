import os

filename = "file.txt"
if os.path.exists(filename):
    os.remove(filename)
else:
    raise OSError("File not found") # This will raise an OSError if the file 'file.txt' does not exist

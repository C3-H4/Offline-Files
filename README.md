A Python script designed to synchronize files between a laptop and a server, taking into account network connections.

**Features**
Automatically detects when connected to a specific Wi-Fi network (VM012354)
Scans through files on both the laptop and server, comparing their dates and contents
Copies new or updated files from the laptop to the server, creating directories as needed

**Requirements**
Python 3.x
subprocess, filecmp, and shutil libraries (included in standard library)
Access to the laptop and server file systems
Usage
Clone this repository to your local machine.
Update the laptop_path and server_path variables at the top of the script to match your specific file paths.
Run the script.
Note: This script assumes that the server is connected via a network share (Z:\Software Engineering). Adjust the server_path variable as needed.

**How it Works**
The script uses netsh to detect the current Wi-Fi network and verify if it’s connected to VM012354.
If connected, the script scans through files on both the laptop and server using os.walk() and filecmp.cmp().
It identifies new or updated files by comparing file dates and contents.
The script copies these files from the laptop to the server, creating directories as needed.

**Troubleshooting**
If the script fails to detect the server connection, check if the Wi-Fi network is correctly configured.
Verify that both the laptop and server have access to the same file paths.
By following these steps and adjusting the script to your specific needs, AutoSync can help keep your files in sync between devices.

# p8p

### peer to peer file sharing application

allows for devices to talk to eachother and pass along files on the same internet network

> [!NOTE]
> LAN (local area network) only, WAN (wide area network) will come sometime soon

## how use?

1. Make sure you are on a computer (laptop or desktop)
2. Look at the bottom left or the bottom middle of your screen: if you see 4 squares that look like a window, follow the Microsoft Windows guide below; if not, follow the macOS (if your computer has an apple on it) or the Linux guide

### Windows

1. Open your preferred web-browser, most likely one of these: Firefox, Chrome, Edge, Brave, Opera
2. Click on this link: [Python 3.14](https://www.python.org/ftp/python/3.14.10/python-3.14.10-amd64.exe)
3. Open the downloaded file, follow the instructions provided and remember to tick the box that says ``"Add to PATH"``
4. When Python says it has finished installing, close the window and download this repository by clicking on the green button above this guide, that says "Code", then "Download ZIP"
5. In your preferred web-browser click on the folder icon next to ``"p8p-main.zip"``
6. You should see "File explorer" open, if not; consult with someone near you
7. Now use your computer mouse to right click on the `"p8p-main.zip"` file
8. Press "Extract all" and extract the file to a preferred location
9. Navigate to the folder named `p8p-main`, follow the next steps
10. Double click on ``start.bat``  or open "terminal" and type `python main.py`
11. Repeat steps 1 through 10 on another device, or repeat step 10 on your current device

### Linux

1. Figure out your "distro", if Ubuntu/Mint, open a terminal and type:
`sudo apt install python3`
2. If any other, consult with your preferred AI provider or a colleague to figure out the steps for installing Python
3. When the terminal says Python has successfully installed, minimize the terminal by pressing on the minimize button (should be a button that looks like a minus) and download this repository by clicking on the green button above this guide, that says "Code", then "Download ZIP"
4. Extract the provided .zip file by right-clicking on your computer mouse and selecting "Extract here"
5. Bring the terminal back into view, by clicking on it in the taskbar and navigate to where the folder you just extracted is located by following step 6
6. Type `cd ` (with a space), then drag the extracted `p8p-main` folder into Terminal, and press enter
7. Type `python3 main.py`
8. Repeat steps 1 through 7 on another device, or repeat step 7 on your current device

### macOS

1. Open your web browser and go to [python.org/downloads](https://www.python.org/downloads/)
2. Click **Download Python** and open the downloaded `.pkg` file to install it.
3. Download this repository by clicking on the green button above this guide, that says "Code", then "Download ZIP"
4. Open your Downloads folder and double-click `p8p-main.zip` to extract it
5. Open the **Terminal** app (Press `cmd + space`, then type "terminal" and press enter)
6. Type `cd ` (with a space), then drag the extracted `p8p-main` folder into Terminal, and press enter
7. Type `python3 main.py` and press enter.
8. Repeat steps 1 through 7 on another device, or repeat step 7 on your current device

## Using the app itself

* Once p8p opens, you will see a message saying `"started p8p, hold your horses"`
* Wait until `located peer:` appears in your terminal, which means both devices or "instances" are connected
* If `peer disconnected:` appears, that device has gone offline or left the network; start p8p on it again to reconnect
* If `located peer:` never appears, repeat the installation steps for your device, making sure everything has been done correctly
* Click into your terminal and type in `/help` to see all available commands

### /help

> Displays all available commands

### /dir

> Lists all available files in the peer computers working directory

Usage:

`/dir` or `/dir {folder}`, replacing "{folder}" with a folder provided by `/dir`

> [!NOTE]
> Outputs marked with [f] are files, outputs marked with [d/] are directories (folders)

### /download

> Allows you to download a file from the peer computer

Usage:

`/download {file}`, replacing "{file}" with the filename provided by `/dir`

### /chat

> Allows you to send a message to the peer computer

Usage:

`/chat {message}`

## AI Declaration

* Bug fixes (commented where AI assisted)
* Figuring out TCP/UDP architecture

![Hackatime Badge](https://hackatime-badge.hackclub.com/U0AJ5EZMELW/p8p)
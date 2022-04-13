# img.accords-library.com

## Installation

```bash
git clone https://github.com/Accords-Library/img.accords-library.com.git
cd img.accords-library.com
npm install
```

To install imagemagick, run the following command:
```bash
./install.sh
```

To convert all images run:
(possibly change the source image folder in the script beforehand)
```bash
python3 processAll.py
```
 
To serve the files, run:
```bash
./run_img_server.sh
```

To start the api server, create a .env file and add:
```txt
TOKEN=SET A KEY TO BE USED FOR AUTH BY THE WEBHOOK
PORT=PORT TO USE WHEN RUNNING THE SERVER
```
Then run:
```bash
./run_img_api.sh
```

# HW4
The spider will scrape the famous IT-shop: https://arvutitark.ee.
The spider will go through the subpages and will find the name, price and 
image for the HDD.

Spider finds hdd name, price and picture. 
If hdd has no picture, then picture href is null.
To run this spider and collect data to `hdd_data.json` file use commandline.

One way of running the app
```
pip3 install scrapy
scrapy runspider app.py -o hdd_data.json
```

Use docker  app
```
pip install scrapy
scrapy runspider app.py -o hdd_data.json
```

### Task description

Making a web crawler.

Example output
```json
{"HDD name": "Silicon Power Bolt B10 128 GB, USB 3.1, must", "Price": 33.01, "Image": "https://arvutitark.ee/prodpics/345/345078/thumb200/3665614.png"},
{"HDD name": "TOSHIBA HDD|TOSHIBA|P300|1TB|SATA 3.0|64 MB|7200 rpm|3,5\"|HDWD110UZSVA", "Price": 38.33, "Image": "https://arvutitark.ee/prodpics/389/389968/thumb200/3802429.jpg"},
{"HDD name": "TOSHIBA BULK V300 Video Streaming Hard HDWU105UZSVA", "Price": 38.33, "Image": null},
{"HDD name": "Seagate Barracuda 1TB SATAIII 7200 RPM, 1000 GB, HDD, 64 MB", "Price": 55.9, "Image": "https://arvutitark.ee/prodpics/252/252501/thumb200/1467056.jpg"},
{"HDD name": "Western Digital Caviar Blue 3.5'' 1TB SATA3 7200RPM 64MB", "Price": 44.9, "Image": "https://arvutitark.ee/prodpics/3/3949/thumb200/129517.png"},
{"HDD name": "TOSHIBA P300 HP HDD 500GB Bulk HDWD105UZSVA", "Price": 40.42, "Image": null},
```
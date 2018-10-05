# Process Management App
This is my second GUI app. A small utility app that shows:
- Process ID
- Process Name
- Username of Process Owner

The app gives you the option to click on a process ID and hit the kill button which kills that process. It auto refreshes the UI so the list of process will also get updated automatically.

### Tools:
- Python 3.6
- PyQt5 [GUI Framework]
- psutil [Python library]

### Test:
If you want to test it and not kill your OS process (or do anything dangerous), test it out by clicking on your browser Process ID and click on the Kill button. This should close your browser.

### How to Run:
``` 
$ git clone https://github.com/tiazahmd/promanagement
$ cd promanagement
$ pip install -r `requirements.txt`
$ python3 main.py
```

### Screenshot:
![promanagement Screenshot](#)
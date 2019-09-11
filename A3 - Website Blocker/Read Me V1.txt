Application 3: Website Blocker

Features:
- runs in background as python script
- blocks and unblocks website automatically as per scheduled time

Libraries:
time	 : to run sleep function in order to utilize processor efficiently
datetime : to get current datetime for scheduling tasks


How to use:
01] Download Ver1.pyw and Ver1.py in same folder
02] Install Python 3 
03] In windows, open task scheduler
04] Select create task option from Actions tab
05] In General Tab, Write Name as Website blocker (Or anything else that you want)
06] In General Tab, Check Run with highesty privileges checkbox
07] In Triggers Tab, select new
08] In Triggers Tab, Select on startup in Begin the task
09] In Actions Tab, Select New
10] In Program/script feild, enter location of your pythonw installation
	e.g. : C:\Users\praja\AppData\Local\Programs\Python\Python37\pythonw.exe
11] In Add aguments feild, Write Ver1.pyw
12] In Start in, enter location ov Ver1.pyw file
13] save and exit
14] you can manually run, end and disable the script from task scheduler library

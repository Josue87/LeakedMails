![Supported Python versions](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu)

# **LeakedMails - Check HaveIBeenPwned**

```
                                                                                                            
██╗     ███████╗ █████╗ ██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ██╗██╗     ███████╗
██║     ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝
██║     █████╗  ███████║█████╔╝ █████╗  ██║  ██║██╔████╔██║███████║██║██║     ███████╗
██║     ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██║  ██║██║╚██╔╝██║██╔══██║██║██║     ╚════██║
███████╗███████╗██║  ██║██║  ██╗███████╗██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗███████║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
|                                                 
|__ Check HaveIBeenPwned with Selenium... By @JosueEncinar

```
Consult the HaveIBeenPwned page using Selenium, to check if emails passed in a file have been involved in leaks. Returns the name of the leaks and their dates.

## Requirements

* [Firefox](https://www.mozilla.org/es-ES/firefox/new/): The tool is configured to work with the Firefox browser.
* [Geckodriver](https://github.com/mozilla/geckodriver/releases): You need to add the folder where the driver is located to your PATH.

## Installation:

```
> pip3 install -r requirements.txt
```


## Usage

```
> python3 leakedMails.py -f our_file_with_emails [-v] [-r]
```

## Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)

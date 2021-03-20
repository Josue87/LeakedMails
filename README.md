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

Manually searching for leaks of an email in HaveIBeenPwned is easy and fast, but when we want to do tens or hundreds of checks the work is tedious, so I have developed this small script to automate the search of a list of emails. This script makes use of **Selenium** to make the requests.

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

## Example

We launch the tool:

```
python3 leakedMails.py -f emails.txt -r -v
```

File emails.txt has the following contents:

```
fakemail@outlook.com
fake@noexistmail.com
fakemail@yahoo.es
```
The -v parameter indicates to display results without leaks. And the -r parameter is used to generate a file with the leaked emails. The execution shows us the following result in the terminal:

![Running_LeakedMails](https://user-images.githubusercontent.com/16885065/110012457-d6bbf600-7d20-11eb-8dd4-e1d6282938eb.png)

In the process, Firefox will be executed thanks to Selenium, and you will see something like the following screenshot:

![Selenium_HaveIBeenPwned](https://user-images.githubusercontent.com/16885065/110012626-023ee080-7d21-11eb-89d1-b9e0be8e8203.png)

The report is a .csv file containing 3 columns (email, name and date of the breach where found).

![Results](https://user-images.githubusercontent.com/16885065/110012755-27335380-7d21-11eb-807a-bcd814a44726.png)


## Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)

## Note

This tool is a PoC. If you use the service on a regular basis, I recommend paying for its API. The services have to be maintained.

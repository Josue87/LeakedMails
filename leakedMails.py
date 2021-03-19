from selenium import webdriver
from time import sleep
import argparse
from os.path import isfile, exists
from sys import exit
from datetime import datetime
import csv
from os import sep, mkdir


def banner():
    print("""
                                                                                                            
██╗     ███████╗ █████╗ ██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ██╗██╗     ███████╗
██║     ██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝
██║     █████╗  ███████║█████╔╝ █████╗  ██║  ██║██╔████╔██║███████║██║██║     ███████╗
██║     ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██║  ██║██║╚██╔╝██║██╔══██║██║██║     ╚════██║
███████╗███████╗██║  ██║██║  ██╗███████╗██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗███████║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
|                                                 
|__ Check HaveIBeenPwned with Selenium... By @JosueEncinar

""")

def _write_results(data):
    folder_results = "results"
    if not exists(folder_results):
        mkdir(folder_results)
    file_name = folder_results + sep + str(datetime.timestamp(datetime.now())).split(".")[0] + "_result.csv"
    with open(file_name, mode='w') as results_file:
        result_writer = csv.DictWriter(results_file, fieldnames=['Email', 'Breach', 'Date Breach'])
        result_writer.writeheader()
        for d in data:
            email = d.get("email")
            leaks = d.get("leaks")
            # If there are many results, they have not been saved.
            if not leaks:
                leaks = [{"name": "Many results ...", "date": ""}]
            for leak in leaks:
                result_writer.writerow({"Email": email, "Breach": leak["name"], "Date Breach": leak["date"]})
    print(f"\n[+] Results saved in {file_name}")

def _parse_response(firefox, email, verbose):
    result = None
    try:
        firefox.find_element_by_id("/Breaches")
        print(f"[+] {email} leaked")
        count = 0
        leaked_info = []
        while True:
            try:
                name = firefox.find_element_by_id(f"/Breaches/{count}/Name").text \
                            .replace('Name ', '').replace('"', '')
                date = firefox.find_element_by_id(f"/Breaches/{count}/BreachDate").text \
                            .replace('BreachDate ', '').replace('"', '')
                print(f" |_ {name} ({date})")
                leaked_info.append({"name": name, "date": date})
                count += 1
            except:
                break
        result = {"email": email, "leaks": leaked_info}
    except:
        if verbose:
            print(f"[-] {email} no leaked")
    return result

def main(args):
    email_file = args.file
    url_base = "https://haveibeenpwned.com/unifiedsearch/"
    leaked = []
    banner()

    if not isfile(email_file):
        print(f"{email_file} not found!!!")
        exit(1)
    try:
        firefox = webdriver.Firefox() # geckodriver must be in a folder within our PATH
    except Exception as e:
        print(f"{e}")
        exit(2)
    with open(email_file, "r") as emails:
        try:
            for email in emails.read().split("\n"):
                if email:
                    url = url_base + email.replace("@", "%40")
                    firefox.get(url)
                    sleep(1) # Wait for the page to load
                    result = _parse_response(firefox, email, args.verbose)
                    if result:
                        leaked.append(result)
            firefox.quit()
        except:
            pass
    if leaked and args.report:
        _write_results(leaked)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--file', help="File with emails (1 per line)",required=True)
    parser.add_argument('-v','--verbose', help="Print all results (no leaked included)", action='store_true', default=False)
    parser.add_argument('-r','--report', help="Write results in a csv file in results folder", action='store_true', default=False)
    args = parser.parse_args()
    main(args)
   
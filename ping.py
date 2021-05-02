import threading
import time
import sys
import os

import requests


cc = "clear"
if sys.platform == "win32":
    cc = "cls"


class Ping():
    def __init__(self, url, threads):
        self.target = url
        self.threads = threads
        self.total = [0, 0]

        for thread in range(int(threads)):
            threading.Thread(target=self.ping, args=[url]).start()
            print(f"Thread{thread+1} started!")

        self.display()


    def display(self):
        while True:
            time.sleep(0.1)
            os.system(cc)
            print("Ping")
            print("by @rzet595\n")
            print(f"TARGET URL -> {self.target}")
            print(f"THREADS -> {self.threads}\n")
            print(f"SENT PACKAGES -> {self.total[0]}")
            print(f"ERRORS -> {self.total[1]}")




    def ping(self, url):
        while True:
            code = requests.get(url).status_code

            self.total[0] += 1
            if code > 299 or code < 200:
                self.total[1] += 1


def parse_args():
    parse_args = {}
    args = sys.argv
    for item in range(len(args)):
        if args[item].startswith("--"):
            arg = args[item].replace("--", "")
            value = args[item+1]

            parse_args[arg] = value


    return parse_args


if __name__ == "__main__":
    args = parse_args()
    Ping(args["url"], args["threads"])

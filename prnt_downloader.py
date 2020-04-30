import randomcode
import requests
import sys
from lxml import html

class screenshotDownloader:
    
    def __init__(self, nb):
        print()
        self.toDl = int(nb)
        self.randomiser = randomcode.RandomsiedCode()
        self.baseUrl = "https://prnt.sc/"
        self.code = self.randomiser.getCode()
        self.url = self.getLink()
        self.downloadedImg = 0
        self.failed = 0

    def __str__(self):
        return "Downloaded images : {0} | Failed : {1}".format(self.downloadedImg, self.failed)

    def getLink(self):
        return self.baseUrl + self.code

    def newLink(self):
        self.code = self.randomiser.anotherCode()
        self.url = self.getLink()

    def totalDl(self):
        return self.downloadedImg + self.failed
    
    def downloadCurrent(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        r = requests.get(self.getLink(), headers={'User-Agent': user_agent})
        tree = html.fromstring(r.content)
        imgLink = tree.xpath('/html/body/div[3]/div/img/@src')[0]
        r.close()
        
        if "image" in imgLink:
            with open("saved_screenshots/" + self.code + ".jpeg", "wb") as img:
                imgReq = requests.get(imgLink, headers={'User-Agent': user_agent})
                for chunk in imgReq:
                    img.write(chunk)
                imgReq.close()
            self.downloadedImg += 1
        else:
            self.failed += 1

        print ("Total : " + str(self.totalDl()) + "/" + str(self.toDl) + " | " + str(self) + "\r", end='')
        
    def run(self):
        if self.toDl == -1:
            print("Starting to download.\nPress Ctrl + C to quit\n\n")
            while True:
                self.downloadCurrent()
                self.newLink()
        else:
            print("Starting to check " + str(self.toDl) + " random codes..\n")
            for i in range(self.toDl):
                self.downloadCurrent()
                self.newLink()
        self.bye()
        
    def bye(self):
        print("\n\n[*] Job finished.\n")

bot = screenshotDownloader(sys.argv[1])
try:
    bot.run()
except (KeyboardInterrupt, SystemExit):
    bot.bye()

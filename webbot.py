from subprocess import Popen, PIPE

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
    # Run bot
    Popen(['./venv/bin/python3', 'bot.py'])

    # Run server
    Popen(['./venv/bin/python3', 'webserver.py'], stdout=PIPE).communicate()


if __name__ == '__main__':
    main()

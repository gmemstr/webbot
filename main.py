from multiprocessing import Pool
import os

'''
Todo:
Webserver to serve RSS file
  -> Custom frontend w/ JS parser
    -> DOM parser?
Threads for webserver and bot
Generate JSON alongside RSS
Logging?
Make into custom website for moderating remotely?!

Always: 
Clean up code
'''

if __name__ == '__main__':
    processes = ('bot.py', 'webserver.py')

    def run_process(process):
        os.system('python3 {}'.format(process))

    pool = Pool(processes=2)
    pool.map(run_process, processes)
import logging
import os
import time
from queue import Queue
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

# Initiating log for time tracking
log = logging.getLogger('my-logger')
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# Master is a dictionary of all of the files in a specified dictionary. It is generated when indexing.
# Contains hash table to allow search in linear time
master = {}
# File names of the returned results
results = []
# Stack of items in your directory that need to be searched.
queue = Queue()


class Searching:
    t1 = ''
    t0 = ''

    def __init__(self):
        self.indexing()
        self.threading()
        self.t1 = ''
        self.t0 = ''

# Loops through every file in a specified directory and adds it to the queue
    def indexing(self):
        log.info('Indexing...')
        for roots, dirs, files in os.walk(r'C:\Users'):
            queue.put(roots)

# Attaches everything in the queue to the file list
    def threading(self):

        self.t0 = time.time()

        pool = ThreadPool(multiprocessing.cpu_count())

        files = []
        for i in iter(queue.get, None):
            files.append(i)
            if queue.qsize() == 0:
                break

        pool.map(self.append, files)
        pool.close()
        pool.join()

        self.t1 = time.time()
        log.info("Time elapsed {}".format(self.t1-self.t0))

# Runs a search based on user input
    def search(self, name):
        results.clear()

        def check(target):
            if name in target:
                results.append(target)
        for i in master.values():
            [check(x) for x in i]

    def append(self, target):
        for item in os.listdir(target):
            values = []
            if os.path.isfile(target + '\\' + item):
                values.append(item)
            master[target] = values


Bot = Searching()


# Begins the program, calls the necessary functions in the bot object.
def main():
    item = input("What would you like to find? \n")
    t0 = time.time()
    Bot.search(item)

    t1 = time.time()
    total = t1 - t0
    log.info(total)

    print('Items found: {}'.format(len(results)))
    for i in results:
        print(i)
    main()


main()

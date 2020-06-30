''' Main.py

This file contains the execution point of the program.
This is separated from main program to allow for potential pre-startup processes.

'''


import Application
import logging
APPLICATION_NAME = "Blackjack"

if __name__ == '__main__':
    # Branch test
    # Init logger
    FORMAT = '[%(asctime)-s][%(levelname)5s] %(message)s'
    logging.basicConfig(filename="latest.log", filemode="w", level=logging.DEBUG,
                        format=FORMAT, datefmt='%H:%M:%S')

    logging.info("Execution begin")
    application = Application.Application(APPLICATION_NAME)
    print("Hi")
    application.mainloop()

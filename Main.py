''' Main.py

This file contains the execution point of the program.
This is separated from main program to allow for potential pre-startup processes.

'''

import Controller
import logging
APPLICATION_NAME = "Blackjack"

if __name__ == '__main__':
    FORMAT = '[%(asctime)-s][%(levelname)5s] %(message)s'
    logging.basicConfig(filename="latest.log", filemode="w", level=logging.DEBUG,
                        format=FORMAT, datefmt='%H:%M:%S')

    logging.info("Execution begin")
    controller = Controller.Controller()
    controller.mainloop()

import logging
import time
from multiprocessing import Lock, Pool, current_process, get_logger

import numpy as np

MESSAGE_FMT = '''INFO: Kernel function being executed in {} process.
  Sleeping for {:.3g} seconds
'''

RAND_STR_FMT = '''INFO: Kernel function being executed in {} process.
  Sleeping for {} seconds
  Random string: {}
'''

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

lock = None

# Loggers
logger = get_logger()
handler = logging.StreamHandler()

logger.addHandler(handler)
logger.setLevel(logging.INFO)


def sleep_message_kernel(sleep_time):
    """Displays a message showing the current process and the
    item passed as argument.

    :param lock:
    :param sleep_time:
    :return:
    """
    pid = current_process().name

    message = MESSAGE_FMT.format(pid, sleep_time)

    lock.acquire()
    logger.info(message)
    lock.release()

    time.sleep(sleep_time)

    lock.acquire()
    logger.info('INFO: Finished kernel execution in {}\n'.format(pid))
    lock.release()

    return message


def make_rand_string(length):
    """Make a random string from a set of characters

    :param length:
    :return:
    """
    ran_str = ''.join(
            np.random.choice(np.array(list(CHARS)), length)
    )
    return ran_str


def rand_string_kernel(length):
    """Generates a random string from a set of characters with
    the given length.

    :param length:
    :return:
    """
    pid = current_process().name
    sleep_time = np.random.randint(0, 3)

    ran_str = make_rand_string(length)
    message = MESSAGE_FMT.format(id, sleep_time, ran_str)

    lock.acquire()
    logger.info(message)
    logger.info('INFO: Finished kernel execution in {}\n'.format(pid))
    lock.release()

    return ran_str


def parallel_exec(kernel, data_grid, processes=None):
    """Executes the function over a multiprocessing-lecture ``Pool``
     over the ``data_grid``.

    :param kernel:
    :param data_grid:
    :param processes:
    :return:
    """
    # A lock instance
    lock_ = Lock()

    exec_results = []
    pool = Pool(processes=processes, initializer=init_, initargs=(lock_,))
    with pool:
        enum_imap = pool.imap(kernel, data_grid)
        for result in enum_imap:
            exec_results.append(result)

    return exec_results


def init_(lock_):
    """Initializer for the multiprocessing Pool. Used to make a lock
    available for all the processes as a global variable.

    :param lock_: A logger.
    :return:
    """
    global lock
    lock = lock_


if __name__ == '__main__':
    time_grid = np.linspace(0, 1, 16, dtype=np.float64)
    parallel_exec(sleep_message_kernel, time_grid)

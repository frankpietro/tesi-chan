import os


def create_log_file():
    if os.path.exists("logfile.txt"):
        os.remove("logfile.txt")
    f = open("logfile.txt", "x")
    f.close()


def log_write(message):
    log_mess("(I) ", message)


def log_error(message):
    log_mess("(E) ", message)


def log_end(message):
    log_mess("(S) ", message)


def log_mess(tag, message):
    f = open("logfile.txt", "a")
    f.write(tag + message + "\n")
    f.close()
import time


def useful_function():
    for i in range(5):
        print("I swear I'm useful: {}".format(i))
        time.sleep(1.0)


if __name__ == "__main__":
    useful_function()

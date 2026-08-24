import time


def main():
    print('Hi from week07_08_my_package.', flush=True)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()

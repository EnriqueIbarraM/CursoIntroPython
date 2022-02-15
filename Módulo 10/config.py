def main():
    try:
        configuration = open('config.txt')
    #except FileNotFoundError as err:
        #print("Couldn't find the config.txt file!")
        #print("got a problem trying to read the file:", err)
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")
    except IsADirectoryError:
        print("Found config.txt but it is a Directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()
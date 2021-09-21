from display import Display

def main():
    display = Display()
    display.setup()
    while True:
        display.update()

if __name__ == "__main__":
    main()
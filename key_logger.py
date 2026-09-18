from pynput import keyboard

def on_press(key, injected):
    status = 'fake' if injected else 'real'
    try:
        print(f"- Alphabetic Key: {key.char}, {status}")
    except AttributeError:
        print(f"- Special Key: {key}, {'fake' if injected else ''}")

def on_release(key, injected):
    status = 'fake' if injected else 'real'

    if key == keyboard.Key.esc:
        print(f"Keylogger Stopped by pressing esc.")
        print(f"The pressed key was {status}")
      #Stop Listening
        return False

with keyboard.Listener( 
    on_press=on_press, 
    on_release=on_release) as listener:

    listener.join()

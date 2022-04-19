# Basic GUI For Remote Mouse-Keyboard Server

## Supported OS:
- Windows

***IMPORTANT:*** Your PC and the remote Device must be connected to the same network.

When you press start it will initialize a server on your computer, your local IP will be shown on screen, put it in your remote device browser to connect.

## Note:
The IP shown may not be accurate, if it says service running and you can't connect, try getting your ip address using the `` ipconfig `` in your command prompt.

The only thing you will have to do is to put this IP into your remote device (Mobile device) browser. You will see a screen like this:

![Example Image](https://i.imgur.com/iAFm6dy.png)

From now you can move through the grey area to move the mouse and just touch to click on the desired button.

Use the text box on top to type something on the PC

# Used libraries:
- Tkinter
- Socket
- Subprocess
- [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit):
  -  ``` python3 -m pip install pywhatkit ```

Server is part of Pywhatkit library. This is only a friendly user interface to start and stop it.
## Sense Hat Morse Code

A simple sense hat python script to translate morse code.

### Installation

You will only need the sense hat python library which you can install with this command: (it comes preinstalled on raspberry pi os)

```Shellscript
pip3 install sense_hat
```

### Running 

Run the translator using this command:

```Shellsript
python3 sensehat_morse.py
```

### Controls

You enter the morse code using the five way joystick:

| Control | Description |
| --- | ---|
| ⬆️ | Enters a dot to the morse code |
| ⬇️ | Enters a dash to the morse code |
| ⬅️ | Deleted the last entered symbol |
| ➡️ | Differences letters by adding a space |
| ⚫ | Done with the message |

### Credits

Thanks a lot to [Julian-Nash](https://github.com/Julian-Nash) for providing the [morse code translator](https://github.com/Julian-Nash/python-morse-code-translator) python script.
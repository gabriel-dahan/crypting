from pathlib import Path
from typing import Union

class ROT13(object):

    def __init__(self, text: Union[Path, str], depth: int):
        if isinstance(text, str):
            self.text = text
        elif isinstance(text, Path):
            path = text.absolute()
            with open(path) as f:
                text = f.readlines()
            self.text = ''.join(text)
        self.depth = depth - 1

    def encrypt(self) -> str:  
        result = ''  
        for i in range(len(self.text)):  
            char = self.text[i]  
            if char.isupper():  
                result += chr((ord(char) + self.depth - 64) % 26 + 65)
            else:  
                result += chr((ord(char) + self.depth - 96) % 26 + 97)
        return result

if __name__ == '__main__':
    crypted = ROT13("My name is ~ Slim Shady ~~", 5).encrypt()
    print(crypted)
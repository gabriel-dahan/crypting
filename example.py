from crypt import Key

if __name__ == '__main__':
    # Be careful, you can definitely lose your file if you're trying to decrypt it with the wrong key.
    k = Key("your-key")
    k.fcrypt('example-files/file.txt', out = 'example-files/file.txt.crypt')
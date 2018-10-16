#!/usr/bin/env python

from pilbox.image import Image


def main():
    print("hola mundo")

    Image(Image.open("/tmp/logo-vpn-01.png"))

if __name__ == "__main__":
    main()


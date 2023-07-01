import qrcode

def main():
    link = input("Link: ")

    img = qrcode.make(link)
    type(img)
    img.save('qr.png')

    print("Saving image...")
    print("Saved")

if __name__ == '__main__':
    main()
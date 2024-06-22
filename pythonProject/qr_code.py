import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input('Enter some text ')

        try:
            self.qr.add_data(user_input)
            qr_img = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_img.save(file_name)
            print(f'QR code saved successfully {file_name}')
        except Exception as e:
            print(f'Error: {e}')

def main():
    myqr = MyQR(size=50, padding=10)
    myqr.create_qr(file_name='qrcode.jpg',
                   fg='blue',
                   bg='white')

if __name__ == '__main__':
    main()
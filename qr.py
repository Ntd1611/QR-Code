import qrcode
import image 
import datetime

while True:
    choice = input("Press Start to start generate QR Code. Press Quit to quit: ").lower()
    if choice=="start":
        data = input("Please enter your link that you want to generate QR Code: ")

        qr = qrcode.QRCode(
            version = 5, 
            box_size= 10, 
            border= 5     
        )

        qr.add_data(data)
        qr.make(fit = True)
        image = qr.make_image(fill="black", back_color="white")

        #Get the current date and time
        time = datetime.datetime.now()
        time_str = time.strftime("%Y-%m-%d-%H-%M-%S")
        
        image.save(f"QR-Code_{time_str}.jpg")
        print("QR code image saved")
        continue
    elif choice != "start" and choice != "quit":
        print("Please type Start or Quit to continue!")
    else:
        print("Quit successfully")
        break
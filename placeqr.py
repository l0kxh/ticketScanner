from PIL import Image

# Function to place QR code onto event pass
def place_qr_code(event_pass_path, qr_code_path, position, qr_size):
    event_pass = Image.open(event_pass_path)
    qr_code = Image.open(qr_code_path)
    qr_code = qr_code.resize((qr_size, qr_size))  # Resize the QR code
    event_pass.paste(qr_code, position)
    return event_pass

# Position for placing the QR code on the event pass
position = (1518, 150)  # Example position

# Path to the event pass template
event_pass_template = "new_pass.png"  # Replace with your event pass template filename

# Path to the folder containing QR codes
qr_codes_folder = "extra_qr_codes_count_0/"  # Replace with the path to your folder containing QR codes
for i in range(1201, 1501):
    # Load the QR code image outside the loop
    qr_code_path = qr_codes_folder + f"qr_code_{i}.png"  # Adjust the filename if necessary

    # Specify the desired size for the QR code
    qr_size = 370  # Adjust as needed

    # Place the same resized QR code onto each event pass

    event_pass_with_qr = place_qr_code(event_pass_template, qr_code_path, position, qr_size)
    event_pass_with_qr.save(f"event_pass_with_qr_{i}.png")

print("QR codes placed on event passes successfully!")

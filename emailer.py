import os
import smtplib
import mimetypes
from email.message import EmailMessage
from user import email, password

def send_gmail_pdf(pdf_path):
    # --- CONFIGURATION ---
    # Put your real Gmail address here
    my_gmail = email
    # Paste your 16-character App Password here
    app_password = password
    
    # 1. Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Your Generated PDF Report'
    msg['From'] = my_gmail
    msg['To'] = my_gmail
    msg.set_content('Hello! Please find your Song Set List attached to this email.')

    # 2. Find and read the PDF file
    mime_type, _ = mimetypes.guess_type(pdf_path)
    main_type, sub_type = mime_type.split('/', 1)

    with open(pdf_path, 'rb') as file:
        file_data = file.read()
        file_name = os.path.basename(pdf_path)
        
    # 3. Attach the PDF
    msg.add_attachment(
        file_data, 
        maintype=main_type, 
        subtype=sub_type, 
        filename=file_name
    )

    # 4. Connect to Gmail and send it
    try:
        # Gmail uses port 587 for secure connections
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() # Shakes hands securely with Gmail
            server.login(my_gmail, app_password)
            server.send_message(msg)
        print("Success! The email has been sent.")
    except Exception as error:
        print(f"Something went wrong: {error}")

# --- HOW TO USE IT ---
# Change these lines to test your file and your destination email!
# send_gmail_pdf("my_report.pdf", "where_to_send_it@example.com")
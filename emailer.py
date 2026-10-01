import os
import smtplib
from email.message import EmailMessage

def send_gmail_pdf(pdf_output, email_address, pdf_filename):
    # --- CONFIGURATION ---
    my_email = os.getenv("EMAIL_ADDRESS") 
    app_password = os.getenv("APP_PASSWORD") # Must be your 16-character Google App Password

    # 1. Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Your Generated PDF Set List'
    msg['From'] = str(my_email).strip()
    msg['To'] = email_address
    msg.set_content('Hello! Please find your Song Set List attached to this email.')

    # 2. Read the PDF from the BytesIO buffer
    pdf_output.seek(0)
    file_data = pdf_output.read()
        
    # 3. Attach the PDF
    msg.add_attachment(
        file_data, 
        maintype='application', 
        subtype='pdf', 
        filename=pdf_filename
    )

    # 4. Connect to Gmail and send it securely
    try:
        # Gmail uses port 465 with SMTP_SSL (best for bypassing Render port blocks)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(str(my_email).strip(), str(app_password).strip())
            server.send_message(msg)
        print("Success! The email has been sent.")
    except Exception as error:
        print(f"Something went wrong: {error}")
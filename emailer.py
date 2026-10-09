import os
import smtplib
from email.message import EmailMessage
def send_gmail_pdf(pdf_output, email_address, pdf_filename):
    # --- CONFIGURATION ---
    api_key = os.getenv("MAILJET_API_KEY")
    secret_key = os.getenv("MAILJET_SECRET_KEY")
    sender_email = os.getenv("SENDER_EMAIL")

    # 1. Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Your Generated PDF Set List'
    msg['From'] = str(sender_email).strip()
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

    # 4. Connect to Mailjet and send it securely
    try:
        # Mailjet uses port 465 with SMTP_SSL
        with smtplib.SMTP_SSL("in-v3.mailjet.com", 465) as server:
            server.login(str(api_key).strip(), str(secret_key).strip())
            server.send_message(msg)
        print("Success! The email has been sent.")
    except Exception as error:
        print(f"Something went wrong: {error}")
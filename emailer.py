import os
import smtplib
import mimetypes
from email.message import EmailMessage

def send_gmail_pdf(pdf_output, email_address, pdf_filename):
    # --- CONFIGURATION ---
    # Put your real Gmail address here
    my_gmail = os.getenv("EMAIL_ADDRESS")
    # Paste your 16-character App Password here
    app_password = os.getenv("APP_PASSWORD")

    # 1. Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Your Generated PDF Set List'
    msg['From'] = my_gmail
    msg['To'] = email_address
    msg.set_content('Hello! Please find your Song Set List attached to this email.')

    # 2. Find and read the PDF file
    mime_type, _ = mimetypes.guess_type(pdf_filename)
    main_type, sub_type = mime_type.split('/', 1)

    pdf_output.seek(0)  # Go to the start of the BytesIO buffer
    file_data = pdf_output.read()
    file_name = pdf_filename
        
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
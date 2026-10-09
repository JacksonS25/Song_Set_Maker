import os
import base64
import json
import urllib.request
from urllib.error import URLError, HTTPError

def send_gmail_pdf(pdf_output, email_address, pdf_filename):
    # --- CONFIGURATION ---
    api_key = os.getenv("MAILJET_API_KEY")
    secret_key = os.getenv("MAILJET_SECRET_KEY")
    sender_email = os.getenv("SENDER_EMAIL")

    # 1. Read the PDF from the BytesIO buffer and encode to base64
    pdf_output.seek(0)
    pdf_bytes = pdf_output.read()
    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

    # 2. Prepare the Mailjet API payload
    url = "https://api.mailjet.com/v3.1/send"
    payload = {
        "Messages": [
            {
                "From": {
                    "Email": sender_email,
                    "Name": "Song Set Maker"
                },
                "To": [
                    {
                        "Email": email_address
                    }
                ],
                "Subject": "Your Generated PDF Set List",
                "TextPart": "Hello! Please find your Song Set List attached to this email.",
                "Attachments": [
                    {
                        "ContentType": "application/pdf",
                        "Filename": pdf_filename,
                        "Base64Content": pdf_base64
                    }
                ]
            }
        ]
    }
    
    # 3. Create the HTTP request
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    req.add_header('Content-Type', 'application/json')
    
    # 4. Add Basic Authentication headers using API & Secret keys
    if api_key and secret_key:
        auth_str = f"{api_key}:{secret_key}"
        b64_auth = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
        req.add_header('Authorization', f'Basic {b64_auth}')
    else:
        print("Missing Mailjet API keys in environment variables!")
        return
    
    # 5. Send the request to Mailjet
    try:
        with urllib.request.urlopen(req) as response:
            print("Success! The email has been sent via Mailjet API.")
    except HTTPError as e:
        error_msg = e.read().decode('utf-8')
        print(f"Mailjet API Error: {e.code} - {error_msg}")
    except URLError as e:
        print(f"Failed to reach Mailjet: {e.reason}")
    except Exception as e:
        print(f"Something went wrong: {e}")
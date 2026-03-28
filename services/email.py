import os
import smtplib
from email.message import EmailMessage


class EmailSender:
    SMTP_CONFIG = {
        "gmail": ("smtp.gmail.com", 587),
        "outlook": ("smtp.office365.com", 587),
        "yahoo": ("smtp.mail.yahoo.com", 587),
    }

    def __init__(self, provider, email, password):
        self.smtp_server, self.smtp_port = self.SMTP_CONFIG[provider]
        self.email_user = email
        self.email_password = password
        self.server = None

    def connect(self):
        self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.server.starttls()
        self.server.login(self.email_user, self.email_password)

    def send_email(self, to, subject, content, attachments=None, cc=None, bcc=None):
        if self.server is None:
            raise Exception("❌ Pas connecté au serveur SMTP")

        msg = EmailMessage()
        msg["From"] = self.email_user
        msg["To"] = ", ".join(to) if isinstance(to, list) else to
        msg["Subject"] = subject

        if cc:
            msg["Cc"] = ", ".join(cc) if isinstance(cc, list) else cc

        msg.set_content(content)

        # Pièces jointes
        if attachments:
            for file_path in attachments:
                with open(file_path, "rb") as f:
                    file_data = f.read()
                    file_name = os.path.basename(file_path)

                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name
                )

        # IMPORTANT : inclure tous les destinataires pour l'envoi réel
        recipients = []
        
        if isinstance(to, list):
            recipients.extend(to)
        else:
            recipients.append(to)

        if cc:
            if isinstance(cc, list):
                recipients.extend(cc)
            else:
                recipients.append(cc)

        if bcc:
            if isinstance(bcc, list):
                recipients.extend(bcc)
            else:
                recipients.append(bcc)

        self.server.send_message(msg, to_addrs=recipients)

    def close(self):
        if self.server:
            self.server.quit()

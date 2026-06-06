from __future__ import annotations

import logging
import os
import smtplib
from email.mime.text import MIMEText
from typing import Any

LOGGER = logging.getLogger(__name__)


def send_digest_email(digest: dict[str, Any], config: dict[str, Any]) -> None:
    host = os.getenv("SMTP_HOST")
    port = os.getenv("SMTP_PORT")
    username = os.getenv("SMTP_USERNAME")
    password = os.getenv("SMTP_PASSWORD")
    email_from = os.getenv("EMAIL_FROM")
    email_to = os.getenv("EMAIL_TO")

    missing = [
        name
        for name, value in {
            "SMTP_HOST": host,
            "SMTP_PORT": port,
            "SMTP_USERNAME": username,
            "SMTP_PASSWORD": password,
            "EMAIL_FROM": email_from,
            "EMAIL_TO": email_to,
        }.items()
        if not value
    ]
    if missing:
        LOGGER.warning("Skipping email because required SMTP settings are missing: %s", ", ".join(missing))
        return

    message = MIMEText(digest["plain_text"], "plain", "utf-8")
    message["Subject"] = digest["subject"]
    message["From"] = email_from
    message["To"] = email_to

    try:
        with smtplib.SMTP(host, int(port), timeout=30) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(email_from, [addr.strip() for addr in email_to.split(",") if addr.strip()], message.as_string())
        LOGGER.info("Digest email sent to %s", email_to)
    except Exception as exc:
        LOGGER.warning("Failed to send digest email: %s", exc)

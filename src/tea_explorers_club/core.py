ALLOWED_DOMAINS = ("@example.com", "@resend.dev")


def is_allowed_email(email):
    for domain in ALLOWED_DOMAINS:
        if email.endswith(domain):
            return True
    return False


def add_subscriber(subscribers, email):
    if not is_allowed_email(email):
        raise ValueError("Only @example.com and @resend.dev addresses are allowed.")
    subscribers.append(email)
    return subscribers


def check_issue(issue):
    if "title" not in issue or "body" not in issue:
        return False
    if issue["title"] == "" or issue["body"] == "":
        return False
    return True


def send_practice(issue, subscribers):
    if not check_issue(issue):
        raise ValueError("Issue needs a title and a body.")
    messages = []
    for email in subscribers:
        if not is_allowed_email(email):
            raise ValueError("Refusing to send to a real address: " + email)
        messages.append("Practice copy of '" + issue["title"] + "' sent to " + email)
    return messages

import csv
from datetime import date, timedelta

ALLOWED_DOMAINS = ("@example.com", "@resend.dev")
DATA_FILE = "data/subscribers.csv"


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


def load_subscribers(path=DATA_FILE):
    with open(path, newline="") as file:
        return list(csv.DictReader(file))


def count_subscribers(subscribers):
    return len(subscribers)


def count_by_group(subscribers, group):
    return sum(1 for subscriber in subscribers if subscriber.get("group") == group)


def count_consent(subscribers):
    return sum(
        1
        for subscriber in subscribers
        if subscriber.get("consent") and subscriber.get("consent").lower() != "waitlist form"
    )


def subscribers_joined_since_days(subscribers, days, run_date):
    run_day = date.fromisoformat(run_date)
    start_day = run_day - timedelta(days=days)
    joined = []
    for subscriber in subscribers:
        joined_on = date.fromisoformat(subscriber["joined_on"])
        if joined_on >= start_day and joined_on <= run_day:
            joined.append(subscriber)
    return joined


def subscribers_joined_since(subscribers, since_date, run_date):
    run_day = date.fromisoformat(run_date)
    start_day = date.fromisoformat(since_date)
    joined = []
    for subscriber in subscribers:
        joined_on = date.fromisoformat(subscriber["joined_on"])
        if joined_on >= start_day and joined_on <= run_day:
            joined.append(subscriber)
    return joined


def next_send(run_date):
    run_day = date.fromisoformat(run_date)
    year = run_day.year
    month = run_day.month + 1
    if month == 13:
        month = 1
        year = year + 1
    first_day = date(year, month, 1)
    days_ahead = (7 - first_day.weekday()) % 7
    send_day = first_day + timedelta(days=days_ahead)
    return send_day.isoformat()

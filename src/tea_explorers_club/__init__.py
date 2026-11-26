from tea_explorers_club.core import add_subscriber, send_practice


def main():
    subscribers = []
    add_subscriber(subscribers, "reader@example.com")
    add_subscriber(subscribers, "giftbuyer@example.com")
    issue = {
        "title": "Welcome to Tea Explorers Club",
        "body": "Your first cup starts here.",
    }
    for message in send_practice(issue, subscribers):
        print(message)

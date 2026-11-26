import sys

from tea_explorers_club.core import (
    add_subscriber,
    count_by_group,
    count_consent,
    count_subscribers,
    load_subscribers,
    send_practice,
)


def main():
    if "subscribers" in sys.argv:
        subscribers = load_subscribers()
        print("total", count_subscribers(subscribers))
        print("consent", count_consent(subscribers))
        for group in ("tea-curious", "gift-buyers", "daily-drinkers"):
            print(group, count_by_group(subscribers, group))
        return

    subscribers = []
    add_subscriber(subscribers, "reader@example.com")
    add_subscriber(subscribers, "giftbuyer@example.com")
    issue = {
        "title": "Welcome to Tea Explorers Club",
        "body": "Your first cup starts here.",
    }
    for message in send_practice(issue, subscribers):
        print(message)

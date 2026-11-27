import sys
from datetime import date

from tea_explorers_club.core import (
    add_subscriber,
    count_by_group,
    count_consent,
    count_subscribers,
    load_subscribers,
    next_send,
    send_practice,
    subscribers_joined_since,
    subscribers_joined_since_days,
)


def main():
    run_date = None
    if "--run-date" in sys.argv:
        index = sys.argv.index("--run-date")
        run_date = sys.argv[index + 1]
    else:
        run_date = date.today().isoformat()

    if "subscribers" in sys.argv:
        subscribers = load_subscribers()
        if "--since-days" in sys.argv:
            index = sys.argv.index("--since-days")
            days = int(sys.argv[index + 1])
            joined = subscribers_joined_since_days(subscribers, days, run_date)
            print(len(joined))
            return
        if "--since" in sys.argv:
            index = sys.argv.index("--since")
            since_date = sys.argv[index + 1]
            joined = subscribers_joined_since(subscribers, since_date, run_date)
            print(len(joined))
            return
        print("total", count_subscribers(subscribers))
        print("consent", count_consent(subscribers))
        for group in ("tea-curious", "gift-buyers", "daily-drinkers"):
            print(group, count_by_group(subscribers, group))
        return

    if "next-send" in sys.argv:
        print(next_send(run_date))
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

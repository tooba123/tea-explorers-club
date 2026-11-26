from tea_explorers_club.core import (
    add_subscriber,
    check_issue,
    count_by_group,
    count_consent,
    count_subscribers,
    is_allowed_email,
    load_subscribers,
    send_practice,
)


def test_allows_example_and_resend_addresses():
    assert is_allowed_email("reader@example.com")
    assert is_allowed_email("practice@resend.dev")
    assert not is_allowed_email("real@person.com")


def test_rejects_real_address():
    subscribers = []
    try:
        add_subscriber(subscribers, "real@person.com")
    except ValueError:
        pass
    else:
        assert False
    assert subscribers == []


def test_check_issue_requires_title_and_body():
    assert check_issue({"title": "Welcome", "body": "Hello"})
    assert not check_issue({"title": "Welcome"})
    assert not check_issue({"body": "Hello"})
    assert not check_issue({"title": "", "body": "Hello"})


def test_send_practice_builds_messages():
    subscribers = ["reader@example.com", "practice@resend.dev"]
    messages = send_practice({"title": "Hello", "body": "Body"}, subscribers)
    assert len(messages) == 2
    assert "reader@example.com" in messages[0]
    assert "practice@resend.dev" in messages[1]


def test_total_subscriber_count_is_24():
    assert count_subscribers(load_subscribers()) == 24


def test_group_counts_are_eight_each():
    subscribers = load_subscribers()
    assert count_by_group(subscribers, "tea-curious") == 8
    assert count_by_group(subscribers, "gift-buyers") == 8
    assert count_by_group(subscribers, "daily-drinkers") == 8


def test_total_consent_count_is_24():
    assert count_consent(load_subscribers()) == 24

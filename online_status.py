def online_count(statuses):
    x = statuses.items()
    count = 0
    for key, value in x:
        if value == "online":
            count += 1
    return(count)

status = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

online_count(status)
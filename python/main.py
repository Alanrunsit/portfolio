import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 4, 9)
days_away = next_birthday - today

if next_birthday == today:
    print(bday_messages.random_message)
else:
    print(f"My birthday is {days_away.days} days away!")
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)

print(now_utc.year)
print(now_utc.month)
print(now_utc.day)
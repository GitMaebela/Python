import datetime

def next_election(start_date: datetime.datetime, interval: int) -> datetime.datetime:
    current_date = start_date
    while current_date.year - start_date.year < interval:
        current_date += datetime.timedelta(days=365)
    return current_date

start_date = datetime.datetime(2019, 5, 8)
interval = 5
next_election_date = next_election(start_date, interval)
print(next_election_date)
from datetime import datetime, timedelta

# Subtract five days from the current date
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Five days ago:", five_days_ago)

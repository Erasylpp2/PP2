from datetime import datetime, timedelta

# Calculate the difference between two dates in seconds
date1 = datetime(2022, 2, 1, 12, 0, 0)
date2 = datetime(2022, 2, 1, 12, 0, 30)
difference = date2 - date1
difference_in_seconds = difference.total_seconds()
print("Difference in seconds:", difference_in_seconds)

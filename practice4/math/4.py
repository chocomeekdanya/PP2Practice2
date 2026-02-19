from datetime import datetime

date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 18, 9, 30, 0)

difference = abs(date1 - date2)
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)

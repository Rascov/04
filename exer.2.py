from datetime import datetime

t = "11:20PM"
time_24hrs = datetime.strptime(t, "%I:%M%p")
time_24hrs.strftime("%H:%M")
f"{time_24hrs:%H:%M}"
print(f"{time_24hrs:%H:%M}")

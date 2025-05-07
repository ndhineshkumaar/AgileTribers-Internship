from datetime import datetime

def formatteddatetime():
    now = datetime.now()
    format = now.strftime("Today is %B %d, %Y, and the time is %I:%M %p")
    print(format)

formatteddatetime()

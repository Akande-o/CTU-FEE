current_time = 14.00
alarm_time = 51.00
alert_time = 14.00 + 51.00

if (alert_time // 12)//2 == 0:
    print(alert_time % 12, "am")
else:
    print(alert_time % 12, "pm")

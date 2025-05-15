import random

interval = 0.1

for sleep in [x * 0.05 for x in range(10, 40)]:
    for i in range(20):
        if 4.8 <= ((sleep / 1.5 - interval) * i) <= 5.0:
            print("SUCCESS TIER1")
            print(sleep, i, (sleep / 1.5 - interval) * i)
        if 4.8 <= ((sleep * 1.5 - interval) * i) <= 5.0:
            print("SUCCESS TIER2")
            print(sleep, i, (sleep * 1.5 - interval) * i)

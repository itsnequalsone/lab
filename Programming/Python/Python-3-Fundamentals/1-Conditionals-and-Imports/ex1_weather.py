"""Weather"""

TEMPERATURE = 75
FORECAST = "sunny"

if TEMPERATURE < 80 and FORECAST != "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

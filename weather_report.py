
"""   Weather report   """



import requests

print("\t\t Welcome to the Weather Forecaster \n")
print("\t Just Enter the City you want the weather report for \n")

city_name = input("Enter the name of the City : ")

# Function to Generate Report
def Gen_report(C):
    url = "https://wttr.in/{}?m".format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
Gen_report(city_name)


'''
Einstein Mwase
Harvard edX, CS50P Python
https://cs50.edx.org/python
https://home.edx.org/

CS50P Lecture 8 - Etcetera III (Type Hints)
Continent Quiz Game
Friday, 13th February, 2026
'''

from flask import Flask, render_template, request
import random

app = Flask(__name__)

North_America = ["American Samoa", "Northern Mariana Islands", "Wake Island", "Guam", "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", 
                "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama",
                "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States of America", "US Virgin Islands",
                "Puerto Rico", "Navassa Island"]
South_America = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
America = North_America + South_America
Africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", 
          "Democratic Republic of Congo", "Republic of Congo", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", 
          "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", 
          "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
          "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
Asia = ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", 
        "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal",
        "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Russia", "Saudi Arabia", "Singapore", "South Korea","Sri Lanka", "Syria", "Taiwan", 
        "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"]
Europe = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", 
          "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", 
          "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", 
          "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City",
          "French Polynesia", "Wallis and Futuna", "New Caledonia", "Pitcairn Islands", "Turks and Caicos Islands", "Sint Maarten", "Saba", "Saint Barthelemy", 
          "Saint Martin", "Saint Pierre and Miquelon", "Sint Eustatius", "Montserrat", "Martinique", "Guadeloupe ", "Greenland", "Curacao", "Cayman Islands", 
          "Clipperton Island", "Anguilla", "Aruba", "Bermuda", "Bonaire", "British Virgin Islands", "Falkland Islands", "French Guiana", 
          "South Georgia and the South Sandwich Islands"]
Australia = ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", 
             "Tonga", "Tuvalu", "Vanuatu", "Cook Islands", "Tokelau", "Niue", "Norfolk Island"]
worldCountries = America + Africa + Asia + Europe + Australia

#The source of these country lists is https://www.countries-ofthe-world.com/countries-of-asia.html

def continentCheck(country: str):
    country = country.strip().title()  #Remove leading/trailing spaces and capitalize each word

    if country in America:
        return "America"
    elif country in Africa:
        return "Africa"
    elif country in Asia:
        return "Asia"
    elif country in Europe:
        return "Europe"
    elif country in Australia:
        return "Australia"
    else: 
        return "Unknown"

def checkGuess(guessedContinent: str, comparingCountry: str):
    gContinent = guessedContinent.strip().title()  
    comCountry = comparingCountry.strip().title() 
    
    realContinent = continentCheck(comCountry)

    if gContinent == realContinent:
        return "Correct"
    elif gContinent not in ["America", "Africa", "Asia", "Europe", "Australia"]:
        print("Sorry,", gContinent, "is not a known continent.")
        return "Interesting, but Wrong"
    else:
        return "Wrong"

@app.route("/", methods=["GET", "POST"])    #This is the route for the home page, and it accepts both GET and POST requests
def index():                                #
    randomCountry = random.choice(worldCountries)
    result = None
    realAnswer = None

    if request.method == "POST":            #
        guess = request.form["continent"]   #Get the user's guess from the form
        result = checkGuess(guess, randomCountry)  #Check the user's guess against the random country
        realAnswer = continentCheck(randomCountry)  #Get the correct continent for the random country

    return render_template("index.html", 
                           country=randomCountry, 
                           result=result, 
                           answer=realAnswer)  #Render the index.html template with the random country, result, and correct answer

if __name__ == "__main__":
    app.run(debug=True)

'''continent = input("Which continent is " + randomCountry + " in? ")
result = checkGuess(continent, randomCountry)
continentCheck(randomCountry)
print("Your guess was",result)
print(randomCountry, "is in", continentCheck(randomCountry))'''


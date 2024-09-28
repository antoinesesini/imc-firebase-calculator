import firebase_admin
from firebase_admin import credentials, db
from unidecode import unidecode


# Initialiser l'application Firebase avec le certificat et l'URL de la Realtime Database
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://inf857---tp1---exo1---imc-default-rtdb.firebaseio.com/'
})


def write_data():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    ref = db.reference('users')
    imc = round(weight / (height / 100) ** 2, 2) # Calculate IMC
    ref.push({
        'name': unidecode(name).lower(),
        'weight': weight,
        'height': height,
        'imc': imc
    })
    print(f"Data for {name} added successfully! IMC: {imc}")

# Function to read data from Firebase
def read_data():
    search_name = input("Enter the name to search: ")
    search_name = unidecode(search_name).lower()
    ref = db.reference('users')
    data = ref.get()
    
    # Search in the data
    find = False
    if data:
        for _, value in data.items():
            if value['name'] == search_name:
                print(f"{value['name']}: Weight = {value['weight']} kg, Height = {value['height']} cm, IMC = {value['imc']}")
                find = True
    if (not find) :
        print("No data found for this name.")

# Menu
while True:
    print("\nOptions:")
    print("1. Add data")
    print("2. Read data")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        write_data()
    elif choice == '2':
        read_data()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")
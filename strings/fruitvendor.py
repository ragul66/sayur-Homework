'''3. Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.'''


fruits = ["apple", "orange", "banana"]  # List of fruits the vendor sells

def find_fruit_quantity(request):
    """
    Finds the fruit and its quantity requested by the customer
    """
    words = request.lower().split()  # Split the request into words and convert to lowercase
    for i in range(len(words)):
        if words[i] in fruits:  # If the word is a fruit name
            fruit = words[i]
            if i < len(words) - 1 and words[i + 1].isdigit():  # If there is a number after the fruit name
                quantity = int(words[i + 1])
            else:
                quantity = input(f"How much {fruit} do you want? ")  # Ask for quantity
                quantity = int(quantity) if quantity.isdigit() else 0  # Convert to int or default to 0
            return fruit, quantity
    return None, None  # If no fruit is found

# Example usage:
while True:
    request = input("What do you want to buy? ")
    fruit, quantity = find_fruit_quantity(request)
    if fruit:
        print(f"{quantity}{fruit}")
    else:
        print("Sorry, I didn't understand what you want.")

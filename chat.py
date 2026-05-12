import random

# =====================
# DATA (defined once, at the top)
# =====================
GREETINGS = ["hii", "hello", "hey"]
GREET_RESPONSES = [
    "Hello! How can I help you?",
    "Hey there!",
    "Hi! Nice to see you."
]

FAREWELLS = ["bye", "goodbye", "good bye"]

COMPLAINTS = ["late", "damaged", "refund", "bad", "issues"]
COMPLAINT_RESPONSES = [
    "We apologize for the inconvenience.",
    "Sorry for the issue.",
    "Our team is working on it."
]

GOOD_FEEDBACKS = ["good", "nice", "excellent", "awesome", "amazing"]
BAD_FEEDBACKS = ["bad", "not", "worst", "terrible"]
GOOD_FEEDBACK_RESPONSES = [
    "Thank you for your positive feedback!",
    "We are happy you liked our service."
]
BAD_FEEDBACK_RESPONSES = [
    "We apologize for your bad experience.",
    "We will work on improving our service."
]

ACCOUNT_RESPONSES = {
    "login": "Please check your login credentials.",
    "password": "Try resetting your password.",
    "signup": "Signup is simple and fast.",
    "account": "We are checking your account issue."
}

ORDER_KEYWORDS = {
    "where":   ["where", "location", "track", "tracking", "status"],
    "price":   ["price", "cost", "how much", "amount", "charge", "bill"],
    "details": ["details", "info", "information", "number", "order no"],
    "arrive":  ["arrive", "arrival", "when", "delivery", "time", "eta"],
    "cancel":  ["cancel", "stop", "return", "refund"],
}

ORDER_RESPONSES = {
    "where":   "📦 Your order is on the way! Current location: Dispatch Center.",
    "price":   "💰 Your total bill amount is ₹500.",
    "details": "🧾 Order No: #1001 | Bill No: #B-2024 | Items: 3",
    "arrive":  "🚚 Your order will arrive within 2-3 business days. Thank you for your patience!",
    "cancel":  "❌ To cancel your order, please call 1800-XXX-XXXX or visit our website.",}
def find_Order_intent(user_input):
   user_input = user_input.lower()
   
   for intent, keywords in ORDER_KEYWORDS.items():

     for keyword in keywords:
         if keyword in user_input:
             return intent
         
   return None

# =====================
# HELPER FUNCTION
# =====================
def find_keyword(user_input, keyword_list):
    """Check if any keyword exists in user input. Returns True/False."""
    for word in user_input.split():
        if word in keyword_list:
            return True
    return False


# =====================
# FEATURE FUNCTIONS
# =====================
def handle_complaint(name):
    user_input = input("Bot: Describe your problem: ").lower()
    save_msg(name, name,user_input)
    found = False
    for word in user_input.split():
        if word in COMPLAINTS:
            comp =  random.choice(COMPLAINT_RESPONSES)
            print("Bot!",comp)
            save_msg( name, "Bot",comp)
            found = True
            break
    if not found:
        print("Bot: Sorry, I could not understand your complaint.")


def handle_feedback(name):
    user_input = input("Bot: Please give your feedback: ").lower()
    save_msg(name,name,user_input)
    found = False
    for word in user_input.split():
        if word in GOOD_FEEDBACKS:
            feed =  random.choice(GOOD_FEEDBACK_RESPONSES)
            print("Bot ! ", feed)
            save_msg(name,"Bot",feed)
            found = True
            break
        elif word in BAD_FEEDBACKS:
            print("Bot:", random.choice(BAD_FEEDBACK_RESPONSES))
            found = True
            break
    if not found:
        print("Bot: Sorry, I could not understand your feedback.")


def handle_accounts(name):
    user_input = input("Bot: Describe your account issue: ").lower()
    save_msg(name,name, user_input)
    found = False
    for word in user_input.split():
        if word in ACCOUNT_RESPONSES:
            act = ACCOUNT_RESPONSES[word]
            print("Bot !",act)
            save_msg(name,"Bot",act)
            found = True
            break
    if not found:
        print("Bot: Sorry, I could not understand your account issue.")

def handle_order(name):
    user_input = input(f"\nBot: hello! How can i help you with your order ")
    save_msg(name,name,user_input)
    found = False
       
       
    intent = find_Order_intent(user_input) 
    if intent :
           ord =  ORDER_RESPONSES[intent]
           print("Bot !",ord ,"\n")
           save_msg(name,"Bot ! ",ord)
           found = True
            
            
    if not found :
         print("Bot: Sorry, I could not understand your order issue.")
def save_msg(name, speaker, message):
    with open("chat.txt", "a", encoding="utf-8") as f:
        f.write(f"{speaker} {message}\n")
# =====================
# MAIN PROGRAM
# =====================
def main():
    name = input("Enter your name: ").strip()
    print(f"Bot: Hello {name}! Welcome to our chat system.")

    while True:
        user_input = input(f"\n{name}: ").lower().strip()
        save_msg(name,name ,user_input)

        # Check greetings
        if user_input in GREETINGS:
            response = random.choice(GREET_RESPONSES)
            print(f"Bot ! {response}")
            save_msg(name,"Bot ! ", response)

        # Check farewells
        elif user_input in FAREWELLS:
            print("Bot: Goodbye! Have a nice day. 👋")
            break

        # Show menu on demand or default
        else:
            print("\nBot: What can I help you with?")
            print("  1. Complaint")
            print("  2. Feedback")
            print("  3. Account Issue")
            print("  4. Order Status")
            print("  5. Exit")

            choice = input("Your choice: ").strip()
            save_msg(name ,name,choice)

            if choice == "1":
                handle_complaint(name)
            
            elif choice == "2":
                handle_feedback(name)
                
            elif choice == "3":
                handle_accounts(name)

            elif choice == "4":
                handle_order(name)

            elif choice == "5":
                print("Bot: Goodbye! Have a nice day. 👋")
                break
            else:
                print("Bot: Sorry, I did not understand that choice.")


if __name__ == "__main__":
    main()

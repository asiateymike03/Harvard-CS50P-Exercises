# Ask user for greeting
greeting = input("Greeting: ").strip()

# Evaluating reward
if greeting.lower().startswith("hello"):
    print("$0")
elif greeting.lower().startswith("h") and not greeting.lower().startswith("hello"):
    print("$20")
else:
    print("$100")
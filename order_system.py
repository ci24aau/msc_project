def validate_payment(amount):
    if amount <= 0:
        raise ValueError("Invalid payment amount")
    return True

def process_order(user_id, amount):
    validate_payment(amount)
    total = amount * 1.2
    return total

def main():
    try:
        print("Processing order...")
        total = process_order(101, -50)  # Intentional error
        print("Total:", total)
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
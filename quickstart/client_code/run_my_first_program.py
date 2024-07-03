# File: src/secret_addition_complete.py (as per your configuration)
# This script converts Rupees (INR) to Dollars (USD)

def rupee_to_dollar(amount_inr):
    # Assuming 1 INR = 0.014 USD (rough approximation)
    conversion_rate = 0.014
    amount_usd = amount_inr * conversion_rate
    return amount_usd

def main():
    # Example usage
    rupee_amount = float(input("Enter the amount in Rupees (INR): "))
    dollar_amount = rupee_to_dollar(rupee_amount)
    print(f"{rupee_amount} INR = {dollar_amount} USD")

if __name__ == "__main__":
    main()



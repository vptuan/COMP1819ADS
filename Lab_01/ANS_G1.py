import random

def generate_numbers():
    print("--- COMP 1819 Data Generation ---")
    print("Generating 40 random numbers between 1 and 1,000,000...\n")
    
    # Generate 40 unique random numbers
    dataset = random.sample(range(1, 1000001), 40)
    
    print(dataset)

    print("\n---------------------------------")
    print("Copy the numbers above for your submission.")

if __name__ == "__main__":
    generate_numbers()
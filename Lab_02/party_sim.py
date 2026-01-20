import time

def run_party_simulation(num_guests):
    print(f"\n--- HOSTING A PARTY WITH {num_guests} GUESTS ---")
    
    # Create a list of guests [Guest 0, Guest 1, ... Guest N]
    guest_list = list(range(num_guests))

    # TASK 1: THE VIP CHECK (Constant Time - O(1))
    start = time.time()
    vip = guest_list[0] # We only look at the first person
    end = time.time()
    print(f"[O(1)] Checked VIP: {(end-start)*1000:.4f} ms")

    # TASK 2: ROLL CALL (Linear Time - O(n))
    start = time.time()
    for guest in guest_list:
        pass # Simulate saying "Hello"
    end = time.time()
    print(f"[O(n)] Roll Call:  {(end-start)*1000:.4f} ms")

    # TASK 3: EVERYONE SHAKES HANDS (Quadratic Time - O(n^2))
    print("Starting Handshakes... (Wait for it...)")
    start = time.time()
    handshakes = 0
    for i in guest_list:
        for j in guest_list:
            handshakes += 1 # Simulate a handshake
    end = time.time()
    print(f"[O(n^2)] Handshakes: {(end-start)*1000:.4f} ms")
    print(f"Total handshakes performed: {handshakes}")

if __name__ == "__main__":
    # Run small simulation
    run_party_simulation(10)
    
    # Run large simulation
    # 3000 guests = 9,000,000 handshakes!
    run_party_simulation(3000) 
    
    print("\n---------------------------------")
    print("Copy the results above for your submission.")
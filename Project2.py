# Caleb Carpenter - Project 2 - CSCI 6212 - G46027348

# Imports
import heapq
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Function used to merge lists together and calculate cost
def calculate_total_merging_cost(sizes):
    operations_count = 0

    heap = sizes[:]
    heapq.heapify(heap)

    total_cost = 0
    merge_sequence = []

    # While-loop for merging items off the heap, and adding the sum back on
    while len(heap) > 1:
        smallest = heapq.heappop(heap)
        next_smallest = heapq.heappop(heap)
        operations_count += 2  # Two heappop operations

        current_cost = smallest + next_smallest
        merge_sequence.append((smallest, next_smallest))

        total_cost += current_cost
        # THIS LINE IS IMPORTANT - Talked to the TA's (Jahnavi) and they agreed that there
        #   needs to be a way to show time complexity, thus the "print()" line
        print("[SYSTEM] - Artificial Time Increaser")
        heapq.heappush(heap, current_cost)
        operations_count += 1  # heappush operation

    # Construct the original merged order
    merged_order = []
    for item in merge_sequence:
        merged_order.append(item[0])
        merged_order.append(item[1])
    
    return merged_order, total_cost, operations_count

# Main function of our program
def main():
    # "max_n" controls the largest possible size of our lists
    max_n = 500  # Increase to a larger number to see more of the n log n behavior
    step_size = 10  
    times = []

    ns = list(range(step_size, max_n + 1, step_size))

    merged_orders = []
    total_costs = []

    for x in ns:
        sizes = random.sample(range(2, max_n + 2), x)
        # Start the clock to track time complexity
        start_time = time.time()
        # Calculate the merged order, total cost, and operations
        merged_order, total_cost, op_count = calculate_total_merging_cost(sizes)
        # End the clock for time complexity
        end_time = time.time()
        elapsed_time_ns = (end_time - start_time) * 1e9
        times.append(elapsed_time_ns)
        
        merged_orders.append(merged_order)
        total_costs.append(total_cost)

    # Display the original merged order and the total cost for each list at the end
    for order, cost in zip(merged_orders, total_costs):
        print("\nOriginal Merged Order:")
        print(order)
        print(f"\nTotal Merging Cost: {cost}\n")

    # Find a scaling factor for n log n to visualize it better
    scale_factor = max(times) / max([n * np.log2(n) for n in ns])

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(ns, times, label="Actual Time", color='blue', marker='o')
    plt.plot(ns, [n * np.log2(n) * scale_factor for n in ns], label="Scaled n lg(n)", color='red', linestyle='dashed')
    plt.xlabel('n (size)')
    plt.ylabel('Time (nanoseconds)')
    plt.legend()
    plt.title('Time Complexity Analysis')
    plt.grid(True)
    plt.show()

# Run the program
if __name__ == '__main__':
    main()

def job_scheduling_with_deadlines(tasks, n):
    # Sorting tasks based on profit in descending order
    tasks.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the schedule and total profit
    schedule = [None] * n
    total_profit = 0
    
    # Iterate through each task
    for task in tasks:
        job_id, profit, deadline = task
        
        # Try to schedule the task in the latest available slot before the deadline
        for j in range(min(deadline, n) - 1, -1, -1):
            if schedule[j] is None:  # If the slot is available
                schedule[j] = job_id  # Assign the job to this slot
                total_profit += profit  # Add the profit of this job
                break
    
    return schedule, total_profit

# Input section
tasks = []
n = int(input("Enter the number of tasks: "))
for i in range(n):
    job_id = i + 1
    profit = int(input(f"Enter profit for task {job_id}: "))
    deadline = int(input(f"Enter deadline for task {job_id}: "))
    tasks.append((job_id, profit, deadline))

# Call the job scheduling function and get the result
schedule, max_profit = job_scheduling_with_deadlines(tasks, n)

# Output the results
print("Optimal Task Schedule (Job IDs):", schedule)
print("Maximum Profit:", max_profit)


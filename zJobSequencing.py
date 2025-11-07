# Job Sequencing with Deadlines using Greedy Method

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Step 1: Sort jobs by descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Step 3: Initialize the slots for scheduling
    slots = [-1] * (max_deadline + 1)
    total_profit = 0
    job_sequence = []

    # Step 4: Schedule jobs greedily
    for job in jobs:
        # Find a free slot from job.deadline to 1
        for slot in range(job.deadline, 0, -1):
            if slots[slot] == -1:
                slots[slot] = job.job_id
                job_sequence.append(job.job_id)
                total_profit += job.profit
                break

    # Step 5: Output results
    print("Job sequence for maximum profit:", job_sequence)
    print("Total Profit:", total_profit)


# Example usage
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]

    job_sequencing(jobs)

def jssp_recursive(jobs, num_machines, schedule, machine_times, job_times, depth=0):
    if depth == len(jobs) * len(jobs[0]):
        return max(machine_times)

    job = depth // len(jobs[0])
    task = depth % len(jobs[0])
    machine, duration = jobs[job][task]

    start_time = max(machine_times[machine], job_times[job])
    end_time = start_time + duration

    schedule[machine].append((start_time, end_time, job, task))
    machine_times[machine] = end_time
    job_times[job] = end_time

    result = jssp_recursive(jobs, num_machines, schedule, machine_times, job_times, depth + 1)

    schedule[machine].pop()
    machine_times[machine] = start_time
    job_times[job] = start_time

    return result

# Ejemplo de uso
jobs = [
    [(0, 3), (1, 2), (2, 2)],
    [(0, 2), (2, 1), (1, 4)],
    [(1, 4), (2, 3)]
]
num_machines = 3
schedule = [[] for _ in range(num_machines)]
machine_times = [0] * num_machines
job_times = [0] * len(jobs)

print(jssp_recursive(jobs, num_machines, schedule, machine_times, job_times))

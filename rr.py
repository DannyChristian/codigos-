def jssp_recursive(jobs, num_machines, schedule, machine_times, job_times, depth=0):
    if depth == len(jobs) * len(jobs[0]):
        return max(machine_times)

    job = depth // len(jobs[0])
    task = depth % len(jobs[0])

    if job >= len(jobs) or task >= len(jobs[job]):
        return float('inf')  # Considerar un valor grande si se excede el índice

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

# Ejemplo de uso y ejecución en Visual Studio Code
if __name__ == "__main__":
    # Definir los datos de prueba
    jobs = [
        [(0, 3), (1, 2)],
        [(0, 2), (1, 4)]
    ]
    num_machines = 2
    schedule = [[] for _ in range(num_machines)]
    machine_times = [0] * num_machines
    job_times = [0] * len(jobs)

    # Llamar a la función principal
    result = jssp_recursive(jobs, num_machines, schedule, machine_times, job_times)

    # Mostrar el resultado
    print("Makespan calculado:", result)

import heapq


class Worker:
    def __init__(self, id, finish=0):
        self.id = id
        self.finish = finish

    def __lt__(self, other):
        if self.finish == other.finish:
            return self.id < other.id 
        return self.finish < other.finish
    
    def __gt__(self, other):
        if self.finish == other.finish:
            return self.id > other.id 
        return self.finish > other.finish



def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    worker_queue = [Worker(i) for i in range(n_workers)]

    for job in jobs:
        worker = heapq.heappop(worker_queue)
        result.append((worker.id, worker.finish))
        worker.finish += job
        heapq.heappush(worker_queue, worker)
    return  result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(*job)
#    print(assigned_jobs)

if __name__ == "__main__":
    main()

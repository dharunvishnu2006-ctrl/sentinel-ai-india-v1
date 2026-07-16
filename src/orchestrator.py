import heapq
class Orchestrator:
    def __init__(self):      
        self.tasks = []

    def add_task(self, urgency: int, task: str):        
        heapq.heappush(self.tasks, (urgency, task))

    def next_task(self):       
        if not self.tasks:
            return None
        return heapq.heappop(self.tasks)
    
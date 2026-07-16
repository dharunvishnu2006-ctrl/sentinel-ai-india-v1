from src.agent import Agent

cloudshield = Agent("CloudShield")
autopilot = Agent("AutoPilot")

print(cloudshield)
print(autopilot)

from src.orchestrator import Orchestrator

orch = Orchestrator()
orch.add_task(3, "Routine report")
orch.add_task(1, "Security breach!")
orch.add_task(2, "Dataset profiling done")

print(orch.next_task())
print(orch.next_task())
print(orch.next_task())
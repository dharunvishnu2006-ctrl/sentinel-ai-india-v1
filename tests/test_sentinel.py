import pytest
from src.agent import Agent
from src.orchestrator import Orchestrator
from src.routing import shortest_path

@pytest.mark.asyncio
async def test_agent_receives_message():
    agent = Agent("TestAgent")
    await agent.inbox.put({"type": "alert", "data": "test"})
    
    msg = await agent.receive()
    assert msg == {"type": "alert", "data": "test"}

def test_orchestrator_priority_order():
    orch = Orchestrator()
    orch.add_task(3, "Routine report")
    orch.add_task(1, "Security breach!")
    orch.add_task(2, "Dataset profiling done")

    first = orch.next_task()
    assert first[0] == 1

def test_bfs_finds_shortest_path():
    graph = {
        "CloudShield": ["Sentinel"],
        "Sentinel": ["CloudShield", "AutoPilot"],
        "AutoPilot": ["Sentinel"]
    }
    path = shortest_path(graph, "CloudShield", "AutoPilot")
    assert path == ["CloudShield", "Sentinel", "AutoPilot"]    

def test_unified_status_aggregates():
    from src.api import app

    client = app.test_client()
    response = client.get("/status")
    data = response.get_json()

    assert "cloudshield" in data
    assert "autopilot" in data    

def test_no_path_handled():
    graph = {
        "CloudShield": ["Sentinel"],
        "Sentinel": ["CloudShield", "AutoPilot"],
        "AutoPilot": ["Sentinel"]
    }    
    path = shortest_path(graph, "CloudShield", "UnknownAgent")
    assert path == []

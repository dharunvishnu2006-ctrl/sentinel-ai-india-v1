import streamlit as st
from src.agent import Agent
from src.orchestrator import Orchestrator
from src.routing import shortest_path
import sqlite3

st.set_page_config(
    page_title="Sentinel AI India",
    page_icon="🛰",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.card {
    background-color: #1e293b;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #334155;
}
.metric {
    text-align:center;
    padding:15px;
    background:#111827;
    border-radius:10px;
    border:1px solid #374151;
}
</style>
""", unsafe_allow_html=True)

st.title("🛰 Sentinel AI India — Command Centre")
st.caption("Real-Time Multi-Agent Monitoring Dashboard")

cloudshield = Agent("CloudShield")
autopilot = Agent("AutoPilot")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🤖 Active Agents")
    st.write(cloudshield)
    st.write(autopilot)

orch = Orchestrator()
orch.add_task(3, "Routine Report")
orch.add_task(1, "Security Breach!")
orch.add_task(2, "Dataset Profiling Complete")

with col2:
    st.subheader("⚡ Priority Queue")
    while True:
        task = orch.next_task()
        if task is None:
            break
        urgency, name = task
        st.success(f"Priority {urgency} → {name}")

st.divider()

st.subheader("📊 System Status")

try:
    conn = sqlite3.connect("data/sentinel.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM cloudshield_status ORDER BY id DESC LIMIT 1"
    )
    cloudshield_status = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM autopilot_status ORDER BY id DESC LIMIT 1"
    )
    autopilot_status = cursor.fetchone()

    conn.close()

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 🛡 CloudShield")
        st.json(cloudshield_status if cloudshield_status else {})

    with c2:
        st.markdown("### 🚀 AutoPilot")
        st.json(autopilot_status if autopilot_status else {})

except Exception as e:
    st.error(f"Database Error: {e}")

st.divider()

st.subheader("🗺 Agent Route Finder")

graph = {
    "CloudShield": ["Sentinel"],
    "Sentinel": ["CloudShield", "AutoPilot"],
    "AutoPilot": ["Sentinel"]
}

left, right = st.columns(2)

with left:
    from_agent = st.text_input("From Agent", "CloudShield")

with right:
    to_agent = st.text_input("To Agent", "AutoPilot")

if st.button("Find Shortest Route", use_container_width=True):
    path = shortest_path(graph, from_agent, to_agent)

    if path:
        st.success(" ➜ ".join(path))
    else:
        st.error("No route found.")
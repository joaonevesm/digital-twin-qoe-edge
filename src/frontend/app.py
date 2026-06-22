import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.backend.data_service import read_telemetry, get_latest_sample
from src.config.settings import DASHBOARD_TITLE

st.set_page_config(page_title="Digital Twin QoE", layout="wide")

st.sidebar.title("Digital Twin QoE")
page = st.sidebar.radio("Navigation", ["Overview", "Network Metrics", "Device Metrics", "QoE Analysis"])
st.sidebar.info("Simulation mode is enabled when no telemetry CSV is found.")

st.title(DASHBOARD_TITLE)
st.caption("Real-time monitoring and QoE assessment for Edge devices.")

df = read_telemetry()
latest = get_latest_sample()

if page == "Overview":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("RSSI", f"{latest['rssi_dbm']} dBm")
    col2.metric("Heap", f"{int(latest['heap_bytes'])} bytes")
    col3.metric("Uptime", f"{int(latest['uptime_s'])} s")
    col4.metric("QoE Score", f"{latest['qoe_score']}/100")

    st.divider()
    col5, col6, col7 = st.columns(3)
    col5.metric("Status", latest["status"])
    col6.metric("Risk Level", latest["risk_level"])
    col7.metric("Recommendation", latest["recommendation"])

    st.subheader("QoE Evolution")
    fig = px.line(df, x="timestamp", y="qoe_score", title="QoE Score Over Time")
    st.plotly_chart(fig, use_container_width=True)

elif page == "Network Metrics":
    st.subheader("Network Signal Monitoring")
    fig = px.line(df, x="timestamp", y="rssi_dbm", title="RSSI Over Time")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df[["timestamp", "rssi_dbm", "qoe_score", "status", "risk_level"]].tail(20), use_container_width=True)

elif page == "Device Metrics":
    st.subheader("Device Resource Monitoring")
    fig = px.line(df, x="timestamp", y="heap_bytes", title="Heap Memory Over Time")
    st.plotly_chart(fig, use_container_width=True)

    if "voltage_v" in df.columns:
        fig2 = px.line(df, x="timestamp", y="voltage_v", title="Voltage Over Time")
        st.plotly_chart(fig2, use_container_width=True)

elif page == "QoE Analysis":
    st.subheader("QoE Engine")
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(latest["qoe_score"]),
        title={"text": "Current QoE Score"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    st.plotly_chart(gauge, use_container_width=True)

    st.markdown("### Decision Rule")
    st.write(
        "The current prototype estimates QoE by combining network quality "
        "(RSSI) and device condition (available heap memory)."
    )

    st.markdown("### Latest Digital Twin State")
    st.json({
        "rssi_dbm": latest["rssi_dbm"],
        "heap_bytes": latest["heap_bytes"],
        "qoe_score": latest["qoe_score"],
        "status": latest["status"],
        "risk_level": latest["risk_level"],
        "recommendation": latest["recommendation"],
    })

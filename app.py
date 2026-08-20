import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Heat Exchanger Design", layout="wide")

st.title("Heat Exchanger Design and Analysis")
st.caption("Core Chemical Engineering Application using Python, Streamlit, and Matplotlib")

with st.sidebar:
    st.header("Process Inputs")
    flow_type = st.radio("Flow Arrangement", ["Counter-current", "Co-current"])

    hot_flow = st.number_input("Hot fluid mass flow rate (kg/s)", value=2.5, min_value=0.1, step=0.1)
    hot_cp = st.number_input("Hot fluid Cp (J/kg·K)", value=2400.0, min_value=100.0, step=50.0)
    hot_in = st.number_input("Hot inlet temperature (°C)", value=120.0, min_value=0.0, step=1.0)
    hot_out = st.number_input("Hot outlet temperature (°C)", value=80.0, min_value=0.0, step=1.0)

    cold_flow = st.number_input("Cold fluid mass flow rate (kg/s)", value=2.0, min_value=0.1, step=0.1)
    cold_cp = st.number_input("Cold fluid Cp (J/kg·K)", value=3000.0, min_value=100.0, step=50.0)
    cold_in = st.number_input("Cold inlet temperature (°C)", value=30.0, min_value=0.0, step=1.0)
    cold_out = st.number_input("Cold outlet temperature (°C)", value=70.0, min_value=0.0, step=1.0)

    u_overall = st.number_input("Overall heat transfer coefficient U (W/m²·K)", value=800.0, min_value=10.0, step=10.0)


def heat_duty(mass_flow, cp, inlet_temp, outlet_temp):
    return mass_flow * cp * (inlet_temp - outlet_temp)


def lmtd_counter(th_in, th_out, tc_in, tc_out):
    delta_t1 = th_in - tc_out
    delta_t2 = th_out - tc_in
    if abs(delta_t1 - delta_t2) < 1e-9:
        return delta_t1
    return (delta_t1 - delta_t2) / np.log(delta_t1 / delta_t2)


def lmtd_parallel(th_in, th_out, tc_in, tc_out):
    delta_t1 = th_in - tc_in
    delta_t2 = th_out - tc_out
    if abs(delta_t1 - delta_t2) < 1e-9:
        return delta_t1
    return (delta_t1 - delta_t2) / np.log(delta_t1 / delta_t2)


hot_q = heat_duty(hot_flow, hot_cp, hot_in, hot_out)
cold_q = heat_duty(cold_flow, cold_cp, cold_out, cold_in)
energy_difference = abs(hot_q - cold_q)

if flow_type == "Counter-current":
    lmt = lmtd_counter(hot_in, hot_out, cold_in, cold_out)
else:
    lmt = lmtd_parallel(hot_in, hot_out, cold_in, cold_out)

area = (hot_q) / (u_overall * lmt)

st.subheader("Energy Balance")
col1, col2, col3 = st.columns(3)
col1.metric("Hot side heat duty (W)", f"{hot_q:,.0f}")
col2.metric("Cold side heat duty (W)", f"{cold_q:,.0f}")
col3.metric("Difference (W)", f"{energy_difference:,.0f}")

if abs(hot_q - cold_q) > 0.05 * max(abs(hot_q), abs(cold_q)):
    st.warning("The energy balance is not close. Adjust flow rates or temperatures for a realistic exchanger design.")
else:
    st.success("The calculated heat duties are reasonably balanced for a preliminary design.")

st.subheader("Heat Exchanger Design Results")
col1, col2, col3 = st.columns(3)
col1.metric("LMTD (°C)", f"{lmt:.2f}")
col2.metric("Overall U (W/m²·K)", f"{u_overall:.1f}")
col3.metric("Required Area (m²)", f"{area:.2f}")

st.subheader("Temperature Profile")
fig, ax = plt.subplots(figsize=(10, 5))

x = np.linspace(0, 1, 100)
hot_temp_profile = np.linspace(hot_in, hot_out, 100)
cold_temp_profile = np.linspace(cold_in, cold_out, 100)

if flow_type == "Counter-current":
    ax.plot(x, hot_temp_profile, label="Hot fluid", color="red", linewidth=2)
    ax.plot(x[::-1], cold_temp_profile, label="Cold fluid", color="blue", linewidth=2)
    ax.set_title("Counter-current Flow Temperature Profile")
else:
    ax.plot(x, hot_temp_profile, label="Hot fluid", color="red", linewidth=2)
    ax.plot(x, cold_temp_profile, label="Cold fluid", color="blue", linewidth=2)
    ax.set_title("Co-current Flow Temperature Profile")

ax.set_xlabel("Exchanger Length")
ax.set_ylabel("Temperature (°C)")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()

st.pyplot(fig)

st.subheader("Summary")

st.markdown(
    f"""
    - Hot fluid heat duty: **{hot_q:,.0f} W**
    - Cold fluid heat duty: **{cold_q:,.0f} W**
    - Log mean temperature difference: **{lmt:.2f} °C**
    - Estimated exchanger area: **{area:.2f} m²**
    - Flow arrangement: **{flow_type}**
    """
)

st.markdown(
    """
    This is a preliminary design estimate for educational and conceptual analysis. An actual process design should include pressure drop, fouling, material selection, and compliance with industrial standards.
    """
)

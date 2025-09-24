# file: planet_weight_app.py
# Run: pip install streamlit
# Then: streamlit run planet_weight_app.py

import streamlit as st

st.set_page_config(page_title="Weight on Other Planets", page_icon="🪐", layout="centered")

st.title("🪐 Weight on Other Planets")
st.write("Enter your weight on **Earth** to know what you'd weigh on other worlds.")

# Approximate surface gravity ratios relative to Earth
GRAVITY = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto (dwarf)": 0.06,
}

with st.form("input"):
    unit = st.selectbox("Unit", ["kg", "lb"], index=0)
    earth_weight = st.number_input(
        f"Your weight on Earth ({unit})", min_value=0.0, value=70.0, step=0.5, format="%.2f"
    )
    selected = st.multiselect(
        "Choose planets (or leave empty to show all)",
        options=list(GRAVITY.keys()),
    )
    submitted = st.form_submit_button("Calculate")

def convert(weight, ratio):
    return weight * ratio

if submitted:
    if earth_weight <= 0:
        st.error("Please enter a weight greater than zero.")
    else:
        rows = []
        targets = selected if selected else GRAVITY.keys()
        for planet in targets:
            ratio = GRAVITY[planet]
            w = convert(earth_weight, ratio)
            rows.append({"Planet": planet, f"Weight ({unit})": round(w, 2), "Gravity×Earth": ratio})
        st.success("Successfully done!")
        st.dataframe(rows, hide_index=True, use_container_width=True)

        # Fun note
        if "Jupiter" in targets and earth_weight > 0:
            st.caption("Fun fact: Did you know that Jupiter’s strong gravity makes you feel more than **2×** as heavy?")

st.divider()
st.caption("These are approximate ratios based on average surface gravity.")

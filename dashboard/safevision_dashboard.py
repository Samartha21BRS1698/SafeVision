# code for dashboard of SafeVsion
import streamlit as st
import pandas as pd
import altair as alt

st.title(" SafeVision Detection Dashboard")

uploaded = st.file_uploader("Upload detection_log.csv", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df.tail(10))

    st.subheader("📊 Detection Trends")
    chart = alt.Chart(df).mark_bar().encode(
        x="class",
        y="count()",
        color="class"
    ).properties(width=600)
    st.altair_chart(chart)

    st.subheader("⏱️ Time-Based Analysis")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    line = alt.Chart(df).mark_line().encode(
        x='timestamp:T',
        y='confidence:Q',
        color='class'
    ).properties(width=600)
    st.altair_chart(line)


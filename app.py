
import streamlit as st
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
st.title("Concrete Strength Probability Explorer")
st.write("Explore the normal distribution of concrete compressive strength.")
mu = st.number_input("Mean (μ)", value=40.0)
sigma = st.number_input("Standard Deviation (σ)", value=5.0)
probability_type = st.selectbox(
    "Select probability type",
    ["Lower Tail", "Upper Tail", "Between"]
)
if probability_type == "Lower Tail":
    x = st.number_input("Enter x", value=30.0)
    z = (x - mu) / sigma
    probability = norm.cdf(z)
    st.write("Z-score =", z)
    st.write("Probability =", probability)
elif probability_type == "Upper Tail":
    x = st.number_input("Enter x", value=50.0)
    z = (x - mu) / sigma
    probability = 1 - norm.cdf(z)
    st.write("Z-score =", z)
    st.write("Probability =", probability)
else:
    x1 = st.number_input("Enter lower bound", value=35.0)
    x2 = st.number_input("Enter upper bound", value=45.0)
    z1 = (x1 - mu) / sigma
    z2 = (x2 - mu) / sigma
    probability = norm.cdf(z2) - norm.cdf(z1)
    st.write("Lower Z-score =", z1)
    st.write("Upper Z-score =", z2)
    st.write("Probability =", probability)
x_values = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
y_values = norm.pdf(x_values, mu, sigma)
fig, ax = plt.subplots()
ax.plot(x_values, y_values)
if probability_type == "Lower Tail":
    ax.fill_between(x_values, y_values, where=(x_values <= x), alpha=0.3)
elif probability_type == "Upper Tail":
    ax.fill_between(x_values, y_values, where=(x_values >= x), alpha=0.3)
else:
    ax.fill_between(x_values, y_values, where=((x_values >= x1) & (x_values <= x2)), alpha=0.3)
ax.set_xlabel("Concrete Compressive Strength (MPa)")
ax.set_ylabel("Probability Density")
st.pyplot(fig)
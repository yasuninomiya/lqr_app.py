import streamlit as st
import numpy as np
from scipy.linalg import solve_continuous_are

st.title("LQR Optimal Regulator Designer")

st.markdown("Enter system matrices A, B and cost matrices Q, R to compute optimal gain K.")

def parse_matrix(text):
    try:
        return np.array(eval(text))
    except:
        return None

A_input = st.text_area("Matrix A (e.g. [[0,1],[-2,-3]])", "[[0, 1], [-2, -3]]")
B_input = st.text_area("Matrix B (e.g. [[0], [1]])", "[[0], [1]]")
Q_input = st.text_area("Matrix Q (e.g. [[1,0],[0,1]])", "[[1, 0], [0, 1]]")
R_input = st.text_area("Matrix R (e.g. [[1]])", "[[1]]")

A = parse_matrix(A_input)
B = parse_matrix(B_input)
Q = parse_matrix(Q_input)
R = parse_matrix(R_input)

if None not in (A, B, Q, R):
    try:
        P = solve_continuous_are(A, B, Q, R)
        K = np.linalg.inv(R) @ B.T @ P
        st.success("Optimal Gain K:")
        st.write(K)
    except Exception as e:
        st.error(f"Error in computation: {e}")
else:
    st.warning("Please enter all matrices in correct format.")

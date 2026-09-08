"""Giving your program a face, option 3: a web page, with Streamlit.

    pip install streamlit
    streamlit run 3_streamlit_page.py

Note the command: NOT python 3_streamlit_page.py. Streamlit runs the file
itself, from top to bottom, every time the user touches something.

Gradio or Streamlit? Gradio thinks in functions, one function equals one page,
and it is the shortest route. Streamlit thinks in scripts, it reads yours line
by line and turns each st.something into an element on the page. Streamlit is
more comfortable when you want several blocks, a table and a chart. Both are
free, both are published in ten minutes.
"""

try:
    import streamlit as st
except ModuleNotFoundError:
    print("streamlit is missing. In the terminal: pip install streamlit")
    print("Then run:  streamlit run 3_streamlit_page.py")
    raise SystemExit(0)


def ctr(impressions, clicks):
    if impressions == 0:
        return 0.0
    return clicks / impressions * 100


def cpa(spend, conversions):
    if conversions == 0:
        return None
    return spend / conversions


# Everything below is the page, written from top to bottom like a document
st.title("Campaign audit")
st.write("Move the numbers and watch the page recompute itself.")

impressions = st.number_input("Impressions", value=283000, step=1000)
clicks = st.number_input("Clicks", value=6792, step=100)
spend = st.number_input("Spend, in euros", value=1450.0, step=50.0)
conversions = st.number_input("Conversions", value=0, step=1)

st.metric("CTR", "%.2f %%" % ctr(impressions, clicks))

cost = cpa(spend, conversions)
if cost is None:
    st.warning("Zero conversions. There is no cost per acquisition to compute here.")
else:
    st.metric("CPA", "%.2f euros" % cost)

st.caption("The two functions above know nothing about this page.")

# What to remember
# 1. streamlit run file.py, never python file.py
# 2. The script is re-run from the top on every interaction. That is the model
# 3. st.title, st.write, st.number_input, st.metric: one call, one element
# 4. Same logic as the Gradio file, same result, a different way of describing it

import streamlit as st

st.set_page_config(page_title="123", page_icon=":cyclone:", layout="wide")

# HEADER SECTION
st.subheader("hello, i am Max :wave:")
st.title("project hopefully")
st.write("123")

from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
st.write(rows)

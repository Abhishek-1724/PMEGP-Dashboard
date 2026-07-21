import streamlit as st

from components.helpers import load_data
from components.sidebar import create_sidebar

from dashboard_pages.executive import executive_dashboard
from dashboard_pages.banks_view import banks_dashboard
from dashboard_pages.geo_view import geographic_dashboard
from dashboard_pages.business_view import business_dashboard
from dashboard_pages.claims_view import claims_dashboard

st.set_page_config(
    page_title="PMEGP Loan Analytics Dashboard",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

try:
    with open("style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

df = load_data()

filtered_df = create_sidebar(df)

page = st.sidebar.radio(
    "📂 Navigation",
    [
        "Executive Dashboard",
        "Bank Analysis",
        "Geographic Analysis",
        "Business Analysis",
        "Claims Dashboard"
    ]
)

if page == "Executive Dashboard":
    executive_dashboard(filtered_df)

elif page == "Bank Analysis":
    banks_dashboard(filtered_df)

elif page == "Geographic Analysis":
    geographic_dashboard(filtered_df)

elif page == "Business Analysis":
    business_dashboard(filtered_df)

elif page == "Claims Dashboard":
    claims_dashboard(filtered_df)

st.markdown("---")

st.caption(
    "PMEGP Loan Analytics & Monitoring Dashboard | Streamlit • Plotly"
)
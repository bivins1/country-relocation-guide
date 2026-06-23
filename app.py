import streamlit as st

from fetch_country import fetch_country
from generate_guide import generate_country_guide
from initialize_gemini import initialize_gemini
from generate_checklist import travel_checklist
from compare_country import compare_countries

from save_guide import save_guide
from save_checklist import save_checklist
from save_comparison import save_comparison


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Country Relocation Guide",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded"
)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div style='text-align:center'>
        <h1 style='color:#2E86AB;'>🌍 Country Relocation Guide</h1>
        <p style='font-size:18px;color:gray;'>
        AI-powered Travel • Study • Relocation Assistant
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown(
    """
    <div style="
        background:#111;
        padding:12px;
        border-radius:10px;
        font-family:monospace;
        color:#00ff88;
    ">
    SYSTEM READY → Choose a feature from the sidebar.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")


# =====================================================
# SIDEBAR NAVIGATION
# =====================================================

option = st.sidebar.selectbox(
    "Navigation",
    [
        "Country Guide",
        "Travel Checklist",
        "Compare Countries",
    ],
)


# =====================================================
# COUNTRY GUIDE
# =====================================================

if option == "Country Guide":

    st.markdown("### 📍 Country Guide Generator")

    country = st.text_input("Enter country name")
    guide_type = st.selectbox("Guide Type", ["vacation", "relocation", "study"])

    if st.button("Generate Guide"):

        if not country:
            st.warning("Please enter a country.")
        else:
            try:
                data = fetch_country(country)

                if not data:
                    st.error("Country not found.")
                else:
                    client = initialize_gemini()

                    guide = generate_country_guide(
                        client,
                        data,
                        guide_type,
                    )

                    st.session_state.latest_guide = {
                        "country": country,
                        "guide_type": guide_type,
                        "content": guide
                    }

            except Exception as e:
                st.error(f"Error: {e}")


    if "latest_guide" in st.session_state:

        guide = st.session_state.latest_guide

        st.success("Guide generated successfully!")
        st.write(guide["content"])

        st.info(
            "⚠️ Important: Download your guide to keep a permanent copy. "
            "Server storage may reset on restart or redeploy."
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Guide"):
                path = save_guide(
                    guide["content"],
                    guide["country"],
                    guide["guide_type"]
                )
                st.success(f"Saved successfully at: {path}")

        with col2:
            st.download_button(
                "⬇ Download Guide",
                guide["content"],
                file_name=f"{guide['country']}_{guide['guide_type']}_guide.txt",
                mime="text/plain"
            )


# =====================================================
# TRAVEL CHECKLIST
# =====================================================

elif option == "Travel Checklist":

    st.markdown("### 🧳 Travel Checklist Generator")

    country = st.text_input("Enter country name", key="checklist_country")
    travel_type = st.selectbox("Purpose", ["vacation", "relocation"])

    if st.button("Generate Checklist"):

        if not country:
            st.warning("Please enter a country.")
        else:
            try:
                checklist = travel_checklist(country, travel_type)

                st.session_state.latest_checklist = {
                    "country": country,
                    "travel_type": travel_type,
                    "content": checklist
                }

            except Exception as e:
                st.error(e)


    if "latest_checklist" in st.session_state:

        checklist = st.session_state.latest_checklist

        st.success("Checklist generated successfully!")
        st.write(checklist["content"])

        st.info(
            "⚠️ Important: Download your checklist to avoid losing it if the app resets."
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Checklist"):
                path = save_checklist(
                    checklist["content"],
                    checklist["country"]
                )
                st.success(f"Saved successfully at: {path}")

        with col2:
            st.download_button(
                "⬇ Download Checklist",
                checklist["content"],
                file_name=f"{checklist['country']}_{checklist['travel_type']}_checklist.txt",
                mime="text/plain"
            )


# =====================================================
# COMPARE COUNTRIES
# =====================================================

elif option == "Compare Countries":

    st.markdown("### ⚖️ Compare Countries")

    col1, col2 = st.columns(2)

    with col1:
        country1 = st.text_input("First Country")

    with col2:
        country2 = st.text_input("Second Country")

    if st.button("Compare Countries"):

        if not country1 or not country2:
            st.warning("Please enter both countries.")
        else:
            try:
                comparison = compare_countries(country1, country2)

                st.session_state.latest_comparison = {
                    "country1": country1,
                    "country2": country2,
                    "content": comparison
                }

            except Exception as e:
                st.error(e)


    if "latest_comparison" in st.session_state:

        comparison = st.session_state.latest_comparison

        st.success("Comparison generated successfully!")
        st.write(comparison["content"])

        st.info(
            "⚠️ Important: Download comparison results to keep a permanent copy."
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Comparison"):
                path = save_comparison(
                    comparison["content"],
                    comparison["country1"],
                    comparison["country2"]
                )
                st.success(f"Saved successfully at: {path}")

        with col2:
            st.download_button(
                "⬇ Download Comparison",
                comparison["content"],
                file_name=f"{comparison['country1']}_vs_{comparison['country2']}.txt",
                mime="text/plain"
            )
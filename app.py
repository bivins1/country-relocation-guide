import streamlit as st

from fetch_country import fetch_country
from generate_guide import generate_country_guide
from initialize_gemini import initialize_gemini
from generate_checklist import travel_checklist
from compare_country import compare_countries


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
# SESSION STATE
# =====================================================

defaults = {
    "saved_guides": {},
    "saved_checklists": {},
    "saved_comparisons": {},
    "latest_guide": None,
    "latest_checklist": None,
    "latest_comparison": None,
    "current_content": None,

    # 🔥 FIX: add status tracking
    "guide_success": False,
    "guide_error": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


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
# SIDEBAR
# =====================================================

option = st.sidebar.selectbox(
    "Navigation",
    [
        "Country Guide",
        "Travel Checklist",
        "Compare Countries",
    ],
)

st.sidebar.markdown("---")
st.sidebar.subheader("💾 Saved Items")


# -------------------------
# Saved Guides
# -------------------------

if st.session_state.saved_guides:
    st.sidebar.markdown("### 📘 Guides")

    for title in st.session_state.saved_guides:
        if st.sidebar.button(title, key=f"guide_{title}"):
            st.session_state.current_content = st.session_state.saved_guides[title]


# -------------------------
# Saved Checklists
# -------------------------

if st.session_state.saved_checklists:
    st.sidebar.markdown("### 🧳 Checklists")

    for title in st.session_state.saved_checklists:
        if st.sidebar.button(title, key=f"checklist_{title}"):
            st.session_state.current_content = st.session_state.saved_checklists[title]


# -------------------------
# Saved Comparisons
# -------------------------

if st.session_state.saved_comparisons:
    st.sidebar.markdown("### ⚖️ Comparisons")

    for title in st.session_state.saved_comparisons:
        if st.sidebar.button(title, key=f"comparison_{title}"):
            st.session_state.current_content = st.session_state.saved_comparisons[title]

# =====================================================
# COUNTRY GUIDE
# =====================================================

if option == "Country Guide":

    st.markdown(
        "<h3 style='color:#F18F01;'>📍 Country Guide Generator</h3>",
        unsafe_allow_html=True,
    )

    country = st.text_input("Enter country name")
    guide_type = st.selectbox("Guide Type", ["vacation", "relocation", "study"])

    if st.button("Generate Guide"):

        # reset state every run
        st.session_state.guide_success = False
        st.session_state.guide_error = None

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
                        "title": f"{country.title()} ({guide_type.title()})",
                        "content": guide,
                        "country": country,
                        "guide_type": guide_type,
                    }

                    # 🔥 FIX: only mark success here
                    st.session_state.guide_success = True

            except Exception as e:
                st.session_state.guide_error = str(e)
                st.session_state.latest_guide = None
                st.error(f"Error generating guide: {e}")


    # =====================================================
    # SAFE DISPLAY BLOCK (FIXED)
    # =====================================================

    if st.session_state.latest_guide:

        guide = st.session_state.latest_guide

        if st.session_state.guide_success and not st.session_state.guide_error:
            st.success("Guide generated successfully!")

        st.write(guide["content"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Guide"):
                st.session_state.saved_guides[guide["title"]] = guide["content"]
                st.success("Guide saved!")

        with col2:
            st.download_button(
                "⬇ Download Guide",
                guide["content"],
                file_name=f"{guide['country'].replace(' ','_')}_{guide['guide_type']}.txt",
                mime="text/plain",
            )


# =====================================================
# TRAVEL CHECKLIST
# =====================================================

elif option == "Travel Checklist":

    st.markdown(
        "<h3 style='color:#1F7A8C;'>🧳 Travel Checklist Generator</h3>",
        unsafe_allow_html=True,
    )

    country = st.text_input("Enter country name", key="checklist_country")

    travel_type = st.selectbox(
        "Purpose",
        ["vacation", "relocation"],
        key="travel_type",
    )

    if st.button("Generate Checklist"):

        if not country:
            st.warning("Please enter a country.")
        else:
            try:
                checklist = travel_checklist(country, travel_type)

                st.session_state.latest_checklist = {
                    "title": f"{country.title()} ({travel_type.title()})",
                    "content": checklist,
                    "country": country,
                    "travel_type": travel_type,
                }

            except Exception as e:
                st.error(e)

    if st.session_state.latest_checklist:

        checklist = st.session_state.latest_checklist

        st.success("Checklist generated successfully!")
        st.write(checklist["content"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Checklist"):
                st.session_state.saved_checklists[checklist["title"]] = checklist["content"]
                st.success("Checklist saved!")

        with col2:
            st.download_button(
                "⬇ Download Checklist",
                checklist["content"],
                file_name=f"{checklist['country'].replace(' ','_')}_{checklist['travel_type']}_checklist.txt",
                mime="text/plain",
            )


# =====================================================
# COMPARE COUNTRIES
# =====================================================

elif option == "Compare Countries":

    st.markdown(
        "<h3 style='color:#6A4C93;'>⚖️ Compare Countries</h3>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        country1 = st.text_input("First Country", key="country1")

    with col2:
        country2 = st.text_input("Second Country", key="country2")

    if st.button("Compare Countries"):

        if not country1 or not country2:
            st.warning("Please enter both countries.")

        else:
            try:
                comparison = compare_countries(country1, country2)

                st.session_state.latest_comparison = {
                    "title": f"{country1.title()} vs {country2.title()}",
                    "content": comparison,
                    "country1": country1,
                    "country2": country2,
                }

            except Exception as e:
                st.error(e)

    if st.session_state.latest_comparison:

        comparison = st.session_state.latest_comparison

        st.success("Comparison generated successfully!")

        st.write(comparison["content"])

        col1, col2 = st.columns(2)

        with col1:

            if st.button("💾 Save Comparison"):

                st.session_state.saved_comparisons[
                    comparison["title"]
                ] = comparison["content"]

                st.success("Comparison saved!")

        with col2:

            st.download_button(
                "⬇ Download Comparison",
                comparison["content"],
                file_name=f"{comparison['country1'].replace(' ','_')}_vs_{comparison['country2'].replace(' ','_')}.txt",
                mime="text/plain",
            )


# =====================================================
# VIEW SAVED ITEM
# =====================================================

if st.session_state.current_content:

    st.markdown("---")
    st.subheader("📖 Saved Item")
    st.write(st.session_state.current_content)
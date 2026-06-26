import streamlit as st
from pathlib import Path

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
# SIDEBAR
# =====================================================

option = st.sidebar.selectbox(
    "Navigation",
    [
        "Country Guide",
        "Travel Checklist",
        "Compare Countries",
        "Saved Files",
    ],
)

st.sidebar.markdown("---")
st.sidebar.subheader("📂 File Management")


# =====================================================
# HELPERS
# =====================================================

def show_files(folder_path: str, title: str):

    st.subheader(title)

    folder = Path(folder_path)

    if not folder.exists():
        st.info("No files found.")
        return

    files = list(folder.glob("*.txt"))

    if not files:
        st.info("No saved files yet.")
        return

    for file in files:

        with st.expander(file.name):

            content = file.read_text(
                encoding="utf-8"
            )

            st.write(content)

            st.download_button(
                "⬇ Download",
                content,
                file_name=file.name,
                mime="text/plain",
                key=f"download_{file.name}"
            )


# =====================================================
# COUNTRY GUIDE
# =====================================================

if option == "Country Guide":

    st.markdown(
        "<h3 style='color:#F18F01;'>📍 Country Guide Generator</h3>",
        unsafe_allow_html=True,
    )

    country = st.text_input(
        "Enter country name"
    )

    guide_type = st.selectbox(
        "Guide Type",
        [
            "vacation",
            "relocation",
            "study"
        ]
    )

    if st.button("Generate Guide"):

        if not country:
            st.warning(
                "Please enter a country."
            )

        else:
            try:

                data = fetch_country(
                    country
                )

                if not data:
                    st.error(
                        "Country not found."
                    )

                else:

                    client = initialize_gemini()

                    guide = generate_country_guide(
                        client,
                        data,
                        guide_type,
                    )

                    st.session_state.guide = {
                        "country": country,
                        "type": guide_type,
                        "content": guide,
                    }

                    st.success(
                        "Guide generated successfully!"
                    )

            except Exception as e:

                st.error(
                    f"Error generating guide: {e}"
                )

    if "guide" in st.session_state:

        guide = st.session_state.guide

        st.write(
            guide["content"]
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Guide"
            ):

                path = save_guide(
                    guide["content"],
                    guide["country"],
                    guide["type"]
                )

                st.success(
                    f"Guide saved successfully at: {path}"
                )

        with col2:

            st.download_button(
                "⬇ Download Guide",
                guide["content"],
                file_name=
                f"{guide['country'].replace(' ','_')}_{guide['type']}_guide.txt",
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

    country = st.text_input(
        "Enter country name",
        key="checklist_country"
    )

    travel_type = st.selectbox(
        "Purpose",
        ["vacation", "relocation"],
        key="travel_type",
    )

    if st.button("Generate Checklist"):

        if not country:

            st.warning(
                "Please enter a country."
            )

        else:

            try:

                checklist = travel_checklist(
                    country,
                    travel_type
                )

                st.session_state.checklist = {
                    "country": country,
                    "type": travel_type,
                    "content": checklist,
                }

                st.success(
                    "Checklist generated successfully!"
                )

            except Exception as e:
                if "checklist" in st.session_state:
                     del st.session_state.checklist

                st.error(e)

    if "checklist" in st.session_state:

        checklist = st.session_state.checklist

        st.write(
            checklist["content"]
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Checklist"
            ):

                path = save_checklist(
                    checklist["content"],
                    checklist["country"]
                )

                st.success(
                    f"Checklist saved successfully at: {path}"
                )

        with col2:

            st.download_button(
                "⬇ Download Checklist",
                checklist["content"],
                file_name=
                f"{checklist['country'].replace(' ','_')}_{checklist['type']}_checklist.txt",
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

        country1 = st.text_input(
            "First Country",
            key="country1"
        )

    with col2:

        country2 = st.text_input(
            "Second Country",
            key="country2"
        )

    if st.button("Compare Countries"):

        if not country1 or not country2:

            st.warning(
                "Please enter both countries."
            )

        else:

            try:

                comparison = compare_countries(
                    country1,
                    country2
                )

                st.session_state.compare = {
                    "country1": country1,
                    "country2": country2,
                    "content": comparison,
                }

                st.success(
                    "Comparison generated successfully!"
                )

            except Exception as e:
                if "compare" in st.session_state:
                    del st.session_state.compare
                st.error(e)

    if "compare" in st.session_state:

        comparison = st.session_state.compare

        st.write(
            comparison["content"]
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Comparison"
            ):

                path = save_comparison(
                    comparison["content"],
                    comparison["country1"],
                    comparison["country2"]
                )

                st.success(
                    f"Comparison saved successfully at: {path}"
                )

        with col2:

            st.download_button(
                "⬇ Download Comparison",
                comparison["content"],
                file_name=
                f"{comparison['country1'].replace(' ','_')}_vs_{comparison['country2'].replace(' ','_')}.txt",
                mime="text/plain",
            )


# =====================================================
# SAVED FILES
# =====================================================

elif option == "Saved Files":

    st.markdown(
        "<h3 style='color:#2E86AB;'>📂 Saved Files</h3>",
        unsafe_allow_html=True,
    )

    st.warning(
        "⚠️ Important: Files saved here are stored on the server. "
        "They may be lost if the app restarts, redeploys, or the "
        "server is reset. Always download important files to your "
        "device for permanent storage."
    )

    show_files(
        "saved_guides",
        "📘 Saved Guides"
    )

    show_files(
        "saved_checklist",
        "🧳 Saved Checklists"
    )

    show_files(
        "saved_comparisons",
        "⚖️ Saved Comparisons"
    )
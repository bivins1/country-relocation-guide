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
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Country Relocation Guide",
    page_icon="🌍",
    layout="centered"
)


# =====================================================
# HEADER
# =====================================================

st.title("🌍 Country Relocation Guide")


# =====================================================
# SIDEBAR
# =====================================================

option = st.sidebar.selectbox(
    "Navigation",
    ["Country Guide", "Travel Checklist", "Compare Countries", "Saved Files"]
)


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

            content = file.read_text(encoding="utf-8")

            st.write(content)

            st.download_button(
                "⬇ Download",
                content,
                file_name=file.name,
                mime="text/plain"
            )


# =====================================================
# COUNTRY GUIDE
# =====================================================

if option == "Country Guide":

    country = st.text_input("Enter country")
    guide_type = st.selectbox("Type", ["vacation", "relocation", "study"])

    if st.button("Generate Guide"):

        if country:
            data = fetch_country(country)
            client = initialize_gemini()

            guide = generate_country_guide(client, data, guide_type)

            st.session_state.guide = {
                "country": country,
                "type": guide_type,
                "content": guide
            }

    if "guide" in st.session_state:

        g = st.session_state.guide

        st.write(g["content"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Guide"):
                path = save_guide(g["content"], g["country"], g["type"])
                st.success(f"Saved successfully at: {path}")

        with col2:
            st.download_button(
                "⬇ Download Guide",
                g["content"],
                file_name=f"{g['country']}_{g['type']}.txt",
                mime="text/plain"
            )


# =====================================================
# CHECKLIST
# =====================================================

elif option == "Travel Checklist":

    country = st.text_input("Country", key="c1")
    ttype = st.selectbox("Purpose", ["vacation", "relocation"])

    if st.button("Generate Checklist"):

        if country:
            checklist = travel_checklist(country, ttype)

            st.session_state.checklist = {
                "country": country,
                "type": ttype,
                "content": checklist
            }

    if "checklist" in st.session_state:

        c = st.session_state.checklist

        st.write(c["content"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Checklist"):
                path = save_checklist(c["content"], c["country"])
                st.success(f"Saved successfully at: {path}")

        with col2:
            st.download_button(
                "⬇ Download Checklist",
                c["content"],
                file_name=f"{c['country']}_{c['type']}_checklist.txt",
                mime="text/plain"
            )


# =====================================================
# COMPARE COUNTRIES
# =====================================================

elif option == "Compare Countries":

    c1 = st.text_input("Country 1")
    c2 = st.text_input("Country 2")

    if st.button("Compare"):

        if c1 and c2:
            result = compare_countries(c1, c2)

            st.session_state.compare = {
                "c1": c1,
                "c2": c2,
                "content": result
            }

    if "compare" in st.session_state:

        cmp = st.session_state.compare

        st.write(cmp["content"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💾 Save Comparison"):
                path = save_comparison(cmp["content"], cmp["c1"], cmp["c2"])
                st.success(f"Saved successfully at: {path}")

        with col2:
            st.download_button(
                "⬇ Download",
                cmp["content"],
                file_name=f"{cmp['c1']}_vs_{cmp['c2']}.txt",
                mime="text/plain"
            )


# =====================================================
# SAVED FILES (SERVER VIEWER)
# =====================================================

elif option == "Saved Files":

    st.warning(
        "⚠️ Important: Files saved here are stored on the server. "
        "They may be lost if the app restarts or redeploys. "
        "Always download important files to your device."
    )

    show_files("saved_guides", "📘 Saved Guides")
    show_files("saved_checklist", "🧳 Saved Checklists")
    show_files("saved_comparisons", "⚖️ Saved Comparisons")
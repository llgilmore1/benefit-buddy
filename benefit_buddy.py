import streamlit as st
import pandas as pd

# Simulated EOB data
eob_data = pd.DataFrame({
    'Date of Service': ['2025-03-01', '2025-03-10', '2025-03-15'],
    'Provider': ['Dr. Smith', 'Radiology Center', 'Therapy Plus'],
    'Service Description': ['Primary Care Visit', 'X-Ray - Knee', 'Physical Therapy'],
    'CPT Code': ['99213', '73560', '97110'],
    'Billed Amount': [150.00, 250.00, 100.00],
    'Allowed Amount': [120.00, 200.00, 90.00],
    'Plan Paid': [90.00, 160.00, 70.00],
    'Member Responsibility': [30.00, 40.00, 20.00],
    'Service Category': ['Primary Care', 'Radiology', 'Rehab Therapy']
})

# Simulated Benefit Usage data
benefit_usage = pd.DataFrame({
    'Benefit Type': ['Primary Care Visits', 'Radiology Services', 'Physical Therapy Sessions'],
    'Annual Limit': [12, 5, 20],
    'Used YTD': [3, 1, 7],
    'Remaining': [9, 4, 13]
})

# Simulated EMR summary
emr_data = pd.DataFrame({
    'Date': ['2025-02-28', '2025-03-01', '2025-03-15'],
    'Diagnosis': ['Hypertension', 'Osteoarthritis - Knee', 'Lower Back Pain'],
    'Medications': ['Lisinopril', 'Ibuprofen', 'Cyclobenzaprine'],
    'Doctor Notes': ['Monitor BP', 'Ordered X-ray', 'Continue PT, reassess in 4 weeks']
})

# Streamlit interface
st.title("Benefit Buddy+ Prototype")

st.header("🧾 Explanation of Benefits (EOB)")
st.dataframe(eob_data)

st.header("📋 Benefit Usage Summary")
st.dataframe(benefit_usage)

st.header("🩺 Patient EMR Snapshot")
st.dataframe(emr_data)

st.header("💡 Suggested Next Steps")
st.write("""
- ✅ Schedule follow-up with PCP to review blood pressure trends.
- 🏋️‍♂️ PT benefits remaining: 13 – consider adding strength training for back.
- 💊 OTC benefit may cover Ibuprofen – check plan.
- 📸 Radiology still has 4 services left – use if knee worsens.
""")
st.header("📁 Upload Your EOB or Plan Document")
uploaded_file = st.file_uploader("Choose a file (PDF, CSV, or TXT)", type=["pdf", "csv", "txt"])

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    st.write("This is where your file will be processed in the next version.")
import fitz  # PyMuPDF

if uploaded_file and uploaded_file.type == "application/pdf":
    st.subheader("📄 PDF Text Extracted:")
    # Read the PDF content
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        st.text_area("PDF Contents", text, height=300)

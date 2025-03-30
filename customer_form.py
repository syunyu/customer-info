import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image
import os
import gspread
from google.oauth2.service_account import Credentials

############# Google Sheets Config #############
SHEET_NAME = "customer_database"  # Google Sheet name

# Authenticate using Streamlit Secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
client = gspread.authorize(credentials)
sheet = client.open(SHEET_NAME).sheet1


############# Show Logo + Title #############
logo = Image.open("logo.jpg")
st.image(logo, use_container_width=True)
st.markdown(
    "<h1 style='text-align: center; margin-top: -60px;'>Customer Information Form</h1>",
    unsafe_allow_html=True
)
############# Phone Formatter #############
def format_phone_number(phone_raw):
    digits = ''.join(filter(str.isdigit, phone_raw))
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    else:
        return phone_raw

############# Get Existing DataFrame #############
def get_existing_data():
    records = sheet.get_all_records()
    return pd.DataFrame(records)

############# Get Next Visit Number #############
def get_next_visit_number(phone_number):
    digits = ''.join(filter(str.isdigit, phone_number))
    if len(digits) != 10:
        return 1, False, pd.DataFrame(), True

    df = get_existing_data()
    if df.empty:
        return 1, False, pd.DataFrame(), True

    df["Phone_digits"] = df["Phone"].astype(str).apply(lambda x: ''.join(filter(str.isdigit, x)))
    matches = df[df["Phone_digits"] == digits]

    if matches.empty:
        return 1, False, pd.DataFrame(), True  # brand new customer

    max_visit = int(matches["This Visit #"].max())
    if max_visit >= 10:
        return max_visit, True, matches.drop(columns="Phone_digits"), False

    return max_visit + 1, False, matches.drop(columns="Phone_digits"), False

############# Session State Init #############
if "form_data" not in st.session_state:
    st.session_state.form_data = {
        "name": "",
        "phone": "",
        "payment": "Cash",
        "visit_date": date.today(),
        "total_amount": "",
        "visit_number": 1
    }

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "clear_form" not in st.session_state:
    st.session_state.clear_form = False

############# Clear Form Logic #############
if st.session_state.clear_form:
    st.session_state.form_data = {
        "name": "",
        "phone": "",
        "payment": "Cash",
        "visit_date": date.today(),
        "total_amount": "",
        "visit_number": 1
    }
    st.session_state.submitted = False
    st.session_state.clear_form = False


############# Input Form #############
with st.form("customer_form"):
    st.session_state.form_data["name"] = st.text_input("Name", value=st.session_state.form_data["name"])
    st.session_state.form_data["phone"] = st.text_input("Phone Number", value=st.session_state.form_data["phone"])
    st.session_state.form_data["payment"] = st.radio("Payment Method", ["Cash", "Credit Card"],
        index=0 if st.session_state.form_data["payment"] == "Cash" else 1)
    st.session_state.form_data["visit_date"] = st.date_input("Date", value=st.session_state.form_data["visit_date"])
    st.session_state.form_data["total_amount"] = st.text_input("Total Amount ($)", value=st.session_state.form_data["total_amount"])

    # Auto-calculate Visit # based on phone number
    phone_input_so_far = st.session_state.form_data["phone"]
    if phone_input_so_far:
        next_visit, max_reached, matched_df, is_new = get_next_visit_number(phone_input_so_far)
        st.session_state.form_data["visit_number"] = next_visit

        if max_reached and not is_new:
            st.warning("‼️ 🎉This customer has visited us 10 times already!🎁")
            st.info("📋 Here are their past 10 visits:")
            st.dataframe(matched_df.sort_values("This Visit #"))

            try:
                avg_total = matched_df["Total Amount"].astype(float).mean()
                st.success(f"💰 Average Total Amount over 10 visits: ${avg_total:.2f}")
            except:
                st.error("❌ Unable to calculate average Total Amount.")

    st.session_state.form_data["visit_number"] = st.number_input("This Visit #", min_value=1, max_value=10,
        value=st.session_state.form_data["visit_number"], disabled=True)

    col1, col2 = st.columns(2)
    submit = col1.form_submit_button("Submit Form提交表格")
    clear = col2.form_submit_button("Clear Form清除表格")

st.markdown("**⚠️注意:** 点击 *提交表格* 提交已输入的信息；清除现有表格内容需点击 *清除表格* 两次后（不可连击，要等待返回再次点击）方可在空白表格进行输入；否则需要手动一行行清除先前输入的信息"）

############# Handle Clear #############
if clear:
    st.session_state.clear_form = True

############# Handle Submit #############
if submit:
    _, max_reached_check, _, is_new_check = get_next_visit_number(st.session_state.form_data["phone"])
    if max_reached_check and not is_new_check:
        st.error("❌ Cannot submit. This customer has already visited 10 times.")
        st.stop()

    if not st.session_state.form_data["name"].strip():
        st.error("❌ Name is required.")
        st.stop()

    digits_only = ''.join(filter(str.isdigit, st.session_state.form_data["phone"]))
    if len(digits_only) != 10:
        st.error("❌ Phone number must contain exactly 10 digits (numbers only).")
        st.stop()

    try:
        total_amount = float(st.session_state.form_data["total_amount"])
    except ValueError:
        st.error("❌ Please enter a valid number for Total Amount.")
        st.stop()

    formatted_phone = format_phone_number(digits_only)

    row = [
        st.session_state.form_data["name"],
        formatted_phone,
        st.session_state.form_data["payment"],
        st.session_state.form_data["visit_date"].strftime("%Y-%m-%d"),
        total_amount,
        st.session_state.form_data["visit_number"]
    ]

    sheet.append_row(row)
    st.session_state.submitted = True
    st.success("🥳 叮！数据已保存成功 ✅ Customer information submitted and saved successfully!")

############# Search Section #############
st.markdown("---")
st.header("🔍 Search Customer Info")

search_option = st.radio("Search by 选择搜索方式（姓名或电话）", ["Name", "Phone Number"])
search_query = st.text_input("Enter search term (姓名不分大小写)")

if st.button("Search"):
    df = get_existing_data()

    if df.empty:
        st.warning("😵‍💫啥也没找到⚠️No customer found")
    else:
        if search_option == "Name":
            results = df[df["Name"].str.contains(search_query, case=False, na=False)]
        else:
            search_digits = ''.join(filter(str.isdigit, search_query))
            df["Phone_digits"] = df["Phone"].astype(str).apply(lambda x: ''.join(filter(str.isdigit, x)))
            results = df[df["Phone_digits"].str.contains(search_digits, na=False)]

        if not results.empty:
            st.success(f"✅ Found {len(results)} result(s):")
            st.dataframe(results.drop(columns="Phone_digits") if "Phone_digits" in results.columns else results)
        else:
            st.warning("😕 啥也没找到 No matching results found")

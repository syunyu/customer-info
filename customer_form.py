import streamlit as st
import pandas as pd
from datetime import date
import os
from openpyxl import load_workbook
from PIL import Image

# ################ Add Usushi Logo ############
logo = Image.open("logo.jpg")
st.image(logo, use_container_width= True) #use_container_width按照原图大小；width可自定义大小数字，比如200/300

# Add Title, margin-top
st.markdown("<h1 style='text-align: center; margin-top: -60px;'>Customer Information Form</h1>",
    unsafe_allow_html=True)


#  ####### format phone number xxx-xxx-xxxx ############
# def format_phone_number(phone_raw):
#     digits = ''.join(filter(str.isdigit, phone_raw))
#     if len(digits) == 10:
#         return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
#     else:
#         return phone_raw  # Leave it as-is if not 10 digits


# ############## streamlit form #############
# from datetime import date
# # default values at top
# if "name" not in st.session_state:
#     st.session_state.name = ""
# if "phone" not in st.session_state:
#     st.session_state.phone = ""
# if "payment" not in st.session_state:
#     st.session_state.payment = "Cash"
# if "visit_date" not in st.session_state:
#     st.session_state.visit_date = date.today()
# if "total_amount" not in st.session_state:
#     st.session_state.total_amount = 0.0
# if "visit_number" not in st.session_state:
#     st.session_state.visit_number = 1


# with st.form("customer_form"):
#     name = st.text_input("Name", value=st.session_state.name, key="name")
#     phone = st.text_input("Phone Number", value=st.session_state.phone, key="phone")
#     payment = st.radio("Payment Method", options=["Cash", "Credit Card"], index=0 if st.session_state.payment == "Cash" else 1, key="payment")
#     visit_date = st.date_input("Date", value=st.session_state.visit_date, key="visit_date")
#     total_amount = st.number_input("Total Amount ($)", min_value=0.0, step=0.01, format="%.2f", value=st.session_state.total_amount, key="total_amount")
#     visit_number = st.number_input("This Visit #", min_value=1, step=1, value=st.session_state.visit_number, key="visit_number")


#     submitted = st.form_submit_button("Submit Form")

#     if submitted:
#         # Format phone number xxx-xxx-xxxx
#         formatted_phone = format_phone_number(phone)

#         # Prepare data to save
#         new_row = {
#             "Name": name,
#             "Phone": formatted_phone,
#             "Payment Method": payment,
#             "Date": visit_date.strftime("%Y-%m-%d"),
#             "Total Amount": total_amount,
#             "This Visit #": visit_number
#         }

#         # --------- Save to Existing Excel File ---------
#         excel_file = "customer_database.xlsx"
#         sheet_name = "customer_database"

#          # If file doesn't exist, create it with correct headers
#         if not os.path.exists(excel_file):
#             df = pd.DataFrame(columns=[
#                 "Name", "Phone", "Payment Method", "Date", "Total Amount", "This Visit #"
#             ])
#             df.to_excel(excel_file, sheet_name=sheet_name, index=False)

#         # Read existing data
#         df_existing = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')

#         # Append new row
#         df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)

#         # Save back to Excel
#         with pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#             df_updated.to_excel(writer, sheet_name=sheet_name, index=False)

#         st.success("🥳 叮！数据已保存成功 ✅ Customer information submitted and saved successfully!")




    ############# Config #############
EXCEL_FILE = "customer_database.xlsx"
SHEET_NAME = "customer_database"
# LOGO_PATH = "/Users/shiyunyu/Desktop/customer_info/logo.jpg"


############# Show Logo + Title #############
# logo = Image.open(LOGO_PATH)
# st.image(logo, use_container_width=True)
# st.markdown(
#     "<h1 style='text-align: center; margin-top: -60px;'>Customer Information Form</h1>",
#     unsafe_allow_html=True
# )

# ############# Phone Formatter #############
# def format_phone_number(phone_raw):
#     digits = ''.join(filter(str.isdigit, phone_raw))
#     if len(digits) == 10:
#         return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
#     else:
#         return phone_raw

# ############# Form State #############
# if "form_data" not in st.session_state:
#     st.session_state.form_data = {
#         "name": "",
#         "phone": "",
#         "payment": "Cash",
#         "visit_date": date.today(),
#         "total_amount": "",
#         "visit_number": 1
#     }

# ############# Form UI #############
# with st.form("customer_form"):
#     st.session_state.form_data["name"] = st.text_input("Name", value=st.session_state.form_data["name"])
#     st.session_state.form_data["phone"] = st.text_input("Phone Number", value=st.session_state.form_data["phone"])
#     st.session_state.form_data["payment"] = st.radio(
#         "Payment Method", options=["Cash", "Credit Card"], index=0 if st.session_state.form_data["payment"] == "Cash" else 1
#     )
#     st.session_state.form_data["visit_date"] = st.date_input("Date", value=st.session_state.form_data["visit_date"])
#     st.session_state.form_data["total_amount"] = st.text_input("Total Amount ($)", value=st.session_state.form_data["total_amount"])
#     st.session_state.form_data["visit_number"] = st.number_input("This Visit #", min_value=1, step=1, value=st.session_state.form_data["visit_number"])

#     col1, col2 = st.columns(2)
#     submit = col1.form_submit_button("Submit Form")
#     clear = col2.form_submit_button("Clear Form")

# ############# Handle Submit #############
# if submit:
#     # Validate name
#     if not st.session_state.form_data["name"].strip():
#         st.error("❌ Name is required.")
#         st.stop()

#     # Validate phone number
#     digits_only = ''.join(filter(str.isdigit, st.session_state.form_data["phone"]))
#     if len(digits_only) != 10:
#         st.error("❌ Phone number must contain exactly 10 digits (numbers only).")
#         st.stop()


#     # Validate total amount
#     try:
#         total_amount = float(st.session_state.form_data["total_amount"])
#     except ValueError: 
#         st.error("❌ Please enter a valid number for Total Amount.")
#         st.stop()

#     formatted_phone = format_phone_number(digits_only)

#     new_row = {
#         "Name": st.session_state.form_data["name"],
#         "Phone": formatted_phone,
#         "Payment Method": st.session_state.form_data["payment"],
#         "Date": st.session_state.form_data["visit_date"].strftime("%Y-%m-%d"),
#         "Total Amount": total_amount,
#         "This Visit #": st.session_state.form_data["visit_number"]
#     }

#     if not os.path.exists(EXCEL_FILE):
#         df = pd.DataFrame(columns=new_row.keys())
#         df.to_excel(EXCEL_FILE, sheet_name=SHEET_NAME, index=False)

#     df_existing = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')
#     df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)

#     with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#         df_updated.to_excel(writer, sheet_name=SHEET_NAME, index=False)

#     st.success("🥳叮！数据已保存成功 ✅ Customer information submitted and saved successfully!")

# ############# Clear Form #############
# if clear:
#     st.session_state.form_data = {
#         "name": "",
#         "phone": "",
#         "payment": "Cash",
#         "visit_date": date.today(),
#         "total_amount": "",
#         "visit_number": 1
#     }

# ########### Add SEARCH FUNCTION ##########
# st.markdown("---")
# st.header("🔍 Search Customer Info")

# search_option = st.radio("Search by 选择搜索方式（姓名或电话）", ["Name", "Phone Number"])
# search_query = st.text_input("Enter search term (搜索词条不分大小写)")

# if st.button("Search"):
#     if not os.path.exists(EXCEL_FILE):
#         st.warning("😵‍💫啥也没找到⚠️No customer found")
#     else:
#         df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')

#         if search_option == "Name":
#             results = df[df["Name"].str.contains(search_query, case=False, na=False)]
#         else:
#             results = df[df["Phone"].str.contains(search_query, na=False)]

#         if not results.empty:
#             st.success(f"Found {len(results)} result(s):")
#             st.dataframe(results)
#         else:
#             st.warning("啥也没找到☹️No matching results found")


# import streamlit as st
# import pandas as pd
# from datetime import date
# from PIL import Image
# import os

# ############# Config #############
# EXCEL_FILE = "customer_database.xlsx"
# SHEET_NAME = "customer_database"

# ############# Phone Formatter #############
# def format_phone_number(phone_raw):
#     digits = ''.join(filter(str.isdigit, phone_raw))
#     if len(digits) == 10:
#         return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
#     else:
#         return phone_raw

# ############# Auto-Calculate Next Visit # #############
# def get_next_visit_number(phone_number):
#     digits = ''.join(filter(str.isdigit, phone_number))
#     if len(digits) != 10 or not os.path.exists(EXCEL_FILE):
#         return 1, False, pd.DataFrame()

#     df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')
#     df["Phone_digits"] = df["Phone"].astype(str).apply(lambda x: ''.join(filter(str.isdigit, x)))
#     matches = df[df["Phone_digits"].str.contains(digits)]

#     if matches.empty:
#         return 1, False  # New customer, start from visit 1

#     max_visit = int(matches["This Visit #"].max())
#     if max_visit >= 10:
#         return max_visit, True  # Max reached, notify with warning

#     return max_visit + 1, False  # Return the next visit number

# ############# Session State Init #############
# if "form_data" not in st.session_state:
#     st.session_state.form_data = {
#         "name": "",
#         "phone": "",
#         "payment": "Cash", 
#         "visit_date": date.today(),
#         "total_amount": "",
#         "visit_number": 1
#     }

# if "submitted" not in st.session_state:
#     st.session_state.submitted = False

# if "clear_form" not in st.session_state:
#     st.session_state.clear_form = False

# ############# Clear Form Logic #############
# if st.session_state.clear_form:
#     st.session_state.form_data = {
#         "name": "",
#         "phone": "",
#         "payment": "Cash",
#         "visit_date": date.today(),
#         "total_amount": "",
#         "visit_number": 1
#     }
#     st.session_state.submitted = False
#     st.session_state.clear_form = False


# ############# Auto-calculate Visit # based on phone number #############
# phone_input_so_far = st.session_state.form_data["phone"]
# if phone_input_so_far:
#     next_visit, max_reached = get_next_visit_number(phone_input_so_far)
#     st.session_state.form_data["visit_number"] = next_visit

#     if max_reached:
#         st.warning("‼️ This customer has visited us 10 times already!")

# ############# Input Form #############
# with st.form("customer_form"):
#     st.session_state.form_data["name"] = st.text_input("Name", value=st.session_state.form_data["name"])
#     st.session_state.form_data["phone"] = st.text_input("Phone Number", value=st.session_state.form_data["phone"])
#     st.session_state.form_data["payment"] = st.radio("Payment Method", ["Cash", "Credit Card"],
#                                                      index=0 if st.session_state.form_data["payment"] == "Cash" else 1)
#     st.session_state.form_data["visit_date"] = st.date_input("Date", value=st.session_state.form_data["visit_date"])
#     st.session_state.form_data["total_amount"] = st.text_input("Total Amount ($)", value=st.session_state.form_data["total_amount"])
#     st.session_state.form_data["visit_number"] = st.number_input("This Visit #", min_value=1, max_value=10, value=st.session_state.form_data["visit_number"], disabled=True)

#     col1, col2 = st.columns(2)
#     submit = col1.form_submit_button("Submit Form")
#     clear = col2.form_submit_button("Clear Form")

# ############# Handle Clear #############
# if clear:
#     st.session_state.clear_form = True

# ############# Handle Submit #############
# if submit:
#     # Validate name
#     if not st.session_state.form_data["name"].strip():
#         st.error("❌ Name is required.")
#         st.stop()

#     # Validate phone number
#     digits_only = ''.join(filter(str.isdigit, st.session_state.form_data["phone"]))
#     if len(digits_only) != 10:
#         st.error("❌ Phone number must contain exactly 10 digits (numbers only).")
#         st.stop()

#     # Validate total amount
#     try:
#         total_amount = float(st.session_state.form_data["total_amount"])
#     except ValueError:
#         st.error("❌ Please enter a valid number for Total Amount.")
#         st.stop()

#     formatted_phone = format_phone_number(digits_only)

#     new_row = {
#         "Name": st.session_state.form_data["name"],
#         "Phone": formatted_phone,
#         "Payment Method": st.session_state.form_data["payment"],
#         "Date": st.session_state.form_data["visit_date"].strftime("%Y-%m-%d"),
#         "Total Amount": total_amount,
#         "This Visit #": st.session_state.form_data["visit_number"]
#     }

#     # Create Excel if needed
#     if not os.path.exists(EXCEL_FILE):
#         df = pd.DataFrame(columns=new_row.keys())
#         df.to_excel(EXCEL_FILE, sheet_name=SHEET_NAME, index=False)

#     # Append data
#     df_existing = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')
#     df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)

#     with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#         df_updated.to_excel(writer, sheet_name=SHEET_NAME, index=False)

#     st.session_state.submitted = True
            
#     ############# Show Success Message #############
# if st.session_state.submitted:
#     st.success("🥳叮！数据已保存成功 ✅ Customer information submitted and saved successfully!")


# # ########### Add SEARCH FUNCTION ##########
# st.markdown("---")
# st.header("🔍 Search Customer Info")

# search_option = st.radio("Search by 选择搜索方式（姓名或电话）", ["Name", "Phone Number"])
# search_query = st.text_input("Enter search term (姓名不分大小写)")

# if st.button("Search"):
#     if not os.path.exists(EXCEL_FILE):
#         st.warning("😵‍💫啥也没找到⚠️No customer found")
#     else:
#         df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')

#         if search_option == "Name":
#             results = df[df["Name"].str.contains(search_query, case=False, na=False)]
#         else:
#             search_digits = ''.join(filter(str.isdigit, search_query))
#             df["Phone_digits"] = df["Phone"].astype(str).apply(lambda x: ''.join(filter(str.isdigit, x)))
#             results = df[df["Phone_digits"].str.contains(search_digits, na=False)]

#         if not results.empty:
#             st.success(f"🥳 Yay! Resultes found ✅ 找到以下记录 {len(results)} 条: ")
#             st.dataframe(results.drop(columns="Phone_digits"))
#         else:
#             st.warning("🤯😵‍💫啥也没找到No matching results found") 

import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image
import os

############# Config #############
EXCEL_FILE = "customer_database.xlsx"
SHEET_NAME = "customer_database"

############# Phone Formatter #############
def format_phone_number(phone_raw):
    digits = ''.join(filter(str.isdigit, phone_raw))
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    else:
        return phone_raw

############# Get Next Visit Number #############
def get_next_visit_number(phone_number):
    digits = ''.join(filter(str.isdigit, phone_number))
    if len(digits) != 10 or not os.path.exists(EXCEL_FILE):
        return 1, False, pd.DataFrame()

    df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')
    df["Phone_digits"] = df["Phone"].astype(str).apply(lambda x: ''.join(filter(str.isdigit, x)))
    matches = df[df["Phone_digits"].str.contains(digits)]

    if matches.empty:
        return 1, False, pd.DataFrame()

    max_visit = int(matches["This Visit #"].max())
    if max_visit >= 10:
        return max_visit, True, matches.drop(columns="Phone_digits")

    return max_visit + 1, False, matches.drop(columns="Phone_digits")

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
        next_visit, max_reached, matched_df = get_next_visit_number(phone_input_so_far)
        st.session_state.form_data["visit_number"] = next_visit

        if max_reached:
            st.warning("‼️ This customer has visited us 10 times already!")
            st.info("📋 Here are their past 10 visits:")
            st.dataframe(matched_df.sort_values("This Visit #"))

            try:
                avg_total = matched_df["Total Amount"].astype(float).mean()
                st.success(f"客人10次消费金额平均值为 💰 Average Total Amount over this 10 visits: ${avg_total:.2f}")
            except:
                st.error("⚠️ Unable to calculate average Total Amount.")


    st.session_state.form_data["visit_number"] = st.number_input("This Visit #", min_value=1, max_value=10,
        value=st.session_state.form_data["visit_number"], disabled=True)

    col1, col2 = st.columns(2)
    submit = col1.form_submit_button("Submit Form")
    clear = col2.form_submit_button("Clear Form")

############# Handle Clear #############
if clear:
    st.session_state.clear_form = True

############# Handle Submit #############
if submit:
    # Block saving if customer already visited 10 times
    _, max_reached_check, _ = get_next_visit_number(st.session_state.form_data["phone"])
    if max_reached_check:
        st.error("❌ Cannot submit. This customer has already visited 10 times.")
        st.stop()

    # Validate name
    if not st.session_state.form_data["name"].strip():
        st.error("❌ Name is required.")
        st.stop()

    # Validate phone number
    digits_only = ''.join(filter(str.isdigit, st.session_state.form_data["phone"]))
    if len(digits_only) != 10:
        st.error("❌ Phone number must contain exactly 10 digits (numbers only).")
        st.stop()

    # Validate total amount
    try:
        total_amount = float(st.session_state.form_data["total_amount"])
    except ValueError:
        st.error("❌ Please enter a valid number for Total Amount.")
        st.stop()

    formatted_phone = format_phone_number(digits_only)

    new_row = {
        "Name": st.session_state.form_data["name"],
        "Phone": formatted_phone,
        "Payment Method": st.session_state.form_data["payment"],
        "Date": st.session_state.form_data["visit_date"].strftime("%Y-%m-%d"),
        "Total Amount": total_amount,
        "This Visit #": st.session_state.form_data["visit_number"]
    }

    # Create Excel if needed
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=new_row.keys())
        df.to_excel(EXCEL_FILE, sheet_name=SHEET_NAME, index=False)

    # Append new data
    df_existing = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')
    df_updated = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)

    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_updated.to_excel(writer, sheet_name=SHEET_NAME, index=False)

    st.session_state.submitted = True
    st.success("🥳叮！数据已保存成功 ✅ Customer information submitted and saved successfully!")


############# Add SEARCH FUNCTION ##########
st.markdown("---")
st.header("🔍 Search Customer Info")

search_option = st.radio("Search by 选择搜索方式（姓名或电话）", ["Name", "Phone Number"])
search_query = st.text_input("Enter search term (姓名不分大小写)")

if st.button("Search"):
    if not os.path.exists(EXCEL_FILE):
        st.warning("😵‍💫啥也没找到⚠️No customer found")
    else:
        df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME, engine='openpyxl')

        if search_option == "Name":
            results = df[df["Name"].str.contains(search_query, case=False, na=False)]
        else:
            search_digits = ''.join(filter(str.isdigit, search_query))
            df["Phone_digits"] = df["Phone"].astype(str).apply(lambda x: ''.join(filter(str.isdigit, x)))
            results = df[df["Phone_digits"].str.contains(search_digits, na=False)]

        if not results.empty:
            st.success(f"🥳 Yay! Resultes found ✅ 找到以下记录 {len(results)} 条: ")
            st.dataframe(results.drop(columns="Phone_digits"))
        else:
            st.warning("🤯😵‍💫啥也没找到No matching results found") 

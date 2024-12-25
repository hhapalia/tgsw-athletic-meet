import streamlit as st
import pandas as pd

st.set_page_config(page_title="Athletic Meet 2024-25")

# Load data from csv into DataFrame
merged_df = pd.read_csv("wadi_combined_2425.csv")

# Streamlit app
st.title("The Galaxy School - Wadi")
st.title("Athletic Meet 2024-25")
st.header("Student Performance App")

# Dropdown to select student
school_list = sorted(merged_df.School.unique())
select_school = st.selectbox("Select School:", options=school_list)

grade_list = sorted(merged_df[merged_df["School"] == select_school].Std.unique())
select_grade = st.selectbox("Select Grade:", options=grade_list)

section_list = sorted(merged_df[(merged_df["School"] == select_school) & (merged_df["Std"] == select_grade)].Sec.unique())
select_section = st.selectbox("Select Section:", options=section_list)

student_list = sorted(merged_df[(merged_df["School"] == select_school) & (merged_df["Std"] == select_grade) & (merged_df["Sec"] == select_section)].Name.unique())
selected_student = st.selectbox("Select Student:", options=student_list)

selected_student_data = merged_df[merged_df["Name"] == selected_student]
grade = selected_student_data["Std"].values[0]
school = selected_student_data["School"].values[0]
unit = selected_student_data["Unit"].values[0]
gender = selected_student_data["Gender"].values[0]
house = selected_student_data["House"].values[0]

# Display selected student's information and performance
# st.write(f"## {selected_student}'s Information:")
# st.write("#### School:", school)
# st.write("#### Gender:", gender)
# st.write("#### House:", house)
# "---"
st.write(f"## {selected_student}'s Performance:")
# st.write("### 100m Time:", str(selected_student_data["100m"].values[0]), "*ss.ms*")
# st.write("### 200m Time:", selected_student_data["200m(s)"].values[0], "*ss.ms OR mm.ss.ms*")
# st.write("### Ball Throw Distance:", selected_student_data["Ball Throw"].values[0], "*mt*")

if grade == 1 or grade == 2 :
    st.dataframe(selected_student_data, column_config={"School": None, "400m": None, "400m(s)": None, "200m(s)": None, "Long Jump": None, "Shot Put":None}, hide_index=True)
elif grade == 3 or grade == 4:
    st.dataframe(selected_student_data, column_config={"School": None, "400m(s)": None, "200m(s)": None, "Long Jump": None, "Shot Put":None}, hide_index=True)
elif grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10 or grade == 11 or grade == 12:
    st.dataframe(selected_student_data, column_config={"School": None, "200m(s)": None, "400m(s)": None}, hide_index=True)


if grade == 1 or grade == 2 :
    st.write("###### 100m Time: *ss.ms*")
    st.write("###### 200m Time: *ss.ms OR m.ss.ms*")
    st.write("###### If any of your event time is displayed as 'None,' it indicates that your performance time was not recorded due to certain reasons.")
elif grade == 3 or grade == 4:
    st.write("###### 100m Time: *ss.ms*")
    st.write("###### 200m Time: *ss.ms OR m.ss.ms*")    
    st.write("###### 400m Time: *m.ss.ms*")
    st.write("###### If any of your event time is displayed as 'None,' it indicates that your performance time was not recorded due to certain reasons.")
elif grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10 or grade == 11 or grade == 12:
    st.write("###### 100m Time: *ss.ms*")
    st.write("###### 200m Time: *ss.ms OR m.ss.ms*")
    st.write("###### 400m Time: *m.ss.ms*")
    st.write("###### Shot Put: *mt*")
    st.write("###### Long Jump: *mt*")
    st.write("###### If any of your event time is displayed as 'None,' it indicates that your performance time was not recorded due to certain reasons.")


"---"

# Display top 8 students for each event in the respective unit and grade level
st.write("## Top 8 students in each event from your Unit:")

if grade == 1 or grade == 2 :
    st.write("### 100m Running")
    table1_100 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","100m"]].nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
    st.dataframe(table1_100, use_container_width=True ,hide_index=True)
    st.write("### 200m Running")
    table1_200 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table1_200, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)

elif grade == 3 or grade == 4:
    st.write("### 100m Running")
    table3_100 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","100m"]].nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
    st.dataframe(table3_100, use_container_width=True ,hide_index=True)
    st.write("### 200m Running")
    table3_200 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table3_200, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### 400m Running")
    table3_400 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","400m","400m(s)"]].nsmallest(8, '400m(s)', keep='all').dropna(subset=['400m(s)'])
    st.dataframe(table3_400, column_config={"400m(s)": None} ,use_container_width=True ,hide_index=True)


elif grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10:
    st.write("### 100m Running")
    table5_100 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","100m"]].nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
    st.dataframe(table5_100, use_container_width=True ,hide_index=True)
    st.write("### 200m Running")
    table5_200 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table5_200, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### 400m Running")
    table5_400 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","400m","400m(s)"]].nsmallest(8, '400m(s)', keep='all').dropna(subset=['400m(s)'])
    st.dataframe(table5_400, column_config={"400m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### Shot Put")
    table5_sp = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Shot Put"]].nlargest(8, 'Shot Put', keep="all").dropna(subset=['Shot Put'])
    st.dataframe(table5_sp, use_container_width=True ,hide_index=True)
    st.write("### Long Jump")
    table5_lj = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Long Jump"]].nlargest(8, 'Long Jump', keep="all").dropna(subset=['Long Jump'])
    st.dataframe(table5_lj, use_container_width=True ,hide_index=True)

elif grade == 11 or grade == 12:
    st.write("### 100m Running")
    table11_100 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","100m"]].nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
    st.dataframe(table11_100, use_container_width=True ,hide_index=True)
    st.write("### 200m Running")
    table11_200 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table11_200, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### 400m Running")
    table11_400 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","400m","400m(s)"]].nsmallest(8, '400m(s)', keep='all').dropna(subset=['400m(s)'])
    st.dataframe(table11_400, column_config={"400m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### Shot Put")
    table11_sp = merged_df[(merged_df["Unit"] == unit) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Shot Put"]].nlargest(8, 'Shot Put', keep="all").dropna(subset=['Shot Put'])
    st.dataframe(table11_sp, use_container_width=True ,hide_index=True)
    st.write("### Long Jump")
    table11_lj = merged_df[(merged_df["Unit"] == unit) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Long Jump"]].nlargest(8, 'Long Jump', keep="all").dropna(subset=['Long Jump'])
    st.dataframe(table11_lj, use_container_width=True ,hide_index=True)

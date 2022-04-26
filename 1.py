import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="123", page_icon=":cyclone:", layout="wide")

# ---- PASSWORD AUTHENTICATION FOR TECHNICAL APPLICATION ----

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Введите пароль", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Введите пароль", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Неверный пароль")
        return False
    else:
        # Password correct.
        return True

with st.sidebar:
	selected = option_menu(
		menu_title="Главное меню",  #required
		options=["Заявка участника", "Техническая заявка", "Ввод результатов"],   #required
		icons=["house", "book", "envelope"],   #optional
		menu_icon="cast",   #optional
		default_index=0,   #optional
	)




# ---- FORM ----
if selected == "Заявка участника":
	st.title(f"{selected}")

#	with st.form("tehz"):
#		st.write("ЗАЯВКА УЧАСТНИКА")
#		st.text_input("Номер участника")
#		st.text_input("Фамилия, имя")
#		st.selectbox("Год рождения", [
#			'2000','2001','2002','2003','2004','2005',
#			'2006','2007','2008','2009','2010',
#			'2011','2012','2013','2014','2015',
#			'2016','2017','2018','2019','2020'])
#		st.text_input("Спортивная организация")
#		st.selectbox("Разряд", [
#			'Без разряда','КМС','1','2','3','1юн','2юн','3юн'])
#		st.multiselect("Дисциплины",[
#			'100м','200м','300м','400м','800м','1500м','3000м',
#			'5000м','100 с барьерами','110 с барьерами','400 с барьерами',
#			'Прыжки в длину','3-ой прыжок с разбега','Толкание ядра',
#			'Метание копья','Эстафета 4 по 100','Эстафета 4 по 400'])
#		st.text_input("Заявленный результат")
#		st.text_input("Тренер(ы)")
#		st.form_submit_button("Отправить")


if selected == "Техническая заявка":
	if check_password():
		st.title(f"{selected}")
		df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vSdVnIuK_edYAl5m_Nuy6LFjxoYZp6j5-zhyOD9U70baFvD6ex5b9WE9nSMJsP3o_mLVWrSZ-4yTEJp/pub?output=xlsx", 
			engine='openpyxl', usecols="B:I")
		st.dataframe(df)

if selected == "Ввод результатов":
	st.title(f"{selected}")


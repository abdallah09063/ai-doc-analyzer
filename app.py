import streamlit as st
from google import genai

st.set_page_config(page_title="AI Analyzer", layout="centered")
st.title("📄 مٌلخّص ومستخرج المهام الذكي")

api_key = st.text_input("أدخل مفتاح Gemini API:", type="password")
user_text = st.text_area("ضع النص هنا:", height=200)

if st.button("تحليل"):
    if not api_key or not user_text:
        st.warning("أدخل المفتاح والنص أولاً.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"لخص هذا النص في نقاط واستخرج المهام المطلوبة منه:\n{user_text}"
            res = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            st.success("تم بنجاح!")
            st.write(res.text)
        except Exception as e:
            st.error(f"خطأ: {e}")
          

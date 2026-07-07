import streamlit as st
from PIL import Image

# 画面のタイトル
st.title("勝馬AIくみこの爆裂自動予想ルーム 🐎🔥")

# 画像のアップロード
uploaded_file = st.file_uploader("馬柱やオッズのスクショを選んでね👇", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # ここで初めてAIのパーツを呼び出す（エラー回避）
    import google.generativeai as genai
    
    image = Image.open(uploaded_file)
    st.image(image, caption="分析中...", use_container_width=True)
    
    # APIキー確認
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        with st.spinner("くみこが分析中...！"):
            response = model.generate_content(["この競馬画像を分析して予想して！", image])
            st.markdown(response.text)
    else:
        st.error("APIキーを入れてね！")

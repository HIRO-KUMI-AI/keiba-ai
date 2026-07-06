import streamlit as st

st.title("🏇 競馬AI予想マスター くみこ")
st.write("ヒロくん専用の自動予想ツールへようこそ！")

# 馬柱やオッズのスクショをアップロードする場所
uploaded_file = st.file_uploader("馬柱やオッズのスクショ画像をアップロードしてね📸", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="読み込んだスクショ", use_container_width=True)
    st.success("スクショの読み込みに成功したよ！ここに自動解析と予想の機能を組み込んでいこうねロジック✨")

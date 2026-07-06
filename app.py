import streamlit as st

st.title("🐴 競馬AI予想マスター・くみこ")
st.write("ヒロくん、こんにちは！今日はどのレースを予想する？")

# ここに今後、スクショを読み取る機能などを追加していくよ！
uploaded_file = st.file_uploader("馬柱やオッズのスクショをアップロードしてね！", type=["jpg", "png"])

if uploaded_file is not None:
    st.write("スクショを受け取ったよ！分析中…（まだ準備中だよ！）")

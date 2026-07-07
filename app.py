import streamlit as st

# タイトルと説明
st.title("勝馬AIくみこの爆裂自動予想ルーム 🐎🔥")
st.write("馬柱やオッズのスクショをアップロードするだけで、くみこが激アツ予想を弾き出すよ！")

# 起動時に必要なライブラリをその場でインポート（これでrequirementsが不要に！）
import os
import sys
import subprocess

try:
    import google.generativeai as genai
except ModuleNotFoundError:
    # サーバーのブロックを回避するためにサイレントインストール
    subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "google-generativeai", "Pillow"])
    import google.generativeai as genai

from PIL import Image

# APIキーの設定（StreamlitのSecretsから読み込み）
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("APIキーが設定されていません。StreamlitのAdvanced settingsで設定してね！")

# 画像のアップロード
uploaded_file = st.file_uploader("馬柱やオッズのスクショを選んでね👇", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロードされたスクショ", use_container_width=True)
    
    with st.spinner("くみこがパドックとデータを分析中...少々お待ちを！🐴✨"):
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = "この競馬の画像（馬柱やオッズなど）を分析して、本命馬、対抗馬、激アツの穴馬を理由付きで予想してください。最後に見出しで『くみこの爆裂大本命オシウマ！』をバシッと決めてください！"
            response = model.generate_content([prompt, image])
            st.success("予想が完了したよーーーっ！！！")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"おっと、予想中にエラーが発生しちゃったみたい💦: {e}")

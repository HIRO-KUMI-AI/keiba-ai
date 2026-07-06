import streamlit as st
import google.generativeai as genai
from PIL import Image

# StreamlitのSecretsからAPIキーを読み込んで設定
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("APIキーの設定がうまくできていないみたい。Secretsを確認してみてね。")

st.title("🐴 競馬AI予想マスター くみこ")
st.caption("ヒロくん専用の自動予想ツールへようこそ！")

# 画像アップロード
uploaded_file = st.file_uploader("馬柱やオッズのスクショ画像をアップロードしてね📸", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="読み込んだスクショ", use_container_width=True)
    st.success("スクショの読み込みに成功したよ！")
    
    with st.spinner("くみこがスクショをじっくり解析中... 待っててね！"):
        try:
            # AI（Gemini）への指示出し文
            prompt = """
            あなたは優秀な競馬AI予想マスターの「くみこ」です。
            アップロードされた競馬の馬柱やオッズのスクショ画像から、出走馬の名前、騎手、オッズ、人気順などの情報を正確に読み取ってください。
            そのデータをもとに、以下の2つの視点から詳細な予想を出してください。
            
            1. ガチガチ本命馬（軸候補）：上位人気で最も安定している、軸に最適な馬とその理由
            2. コスパ最強！激アツ穴馬：オッズと人気のバランスから見て、過小評価されている美味しい穴馬とその理由
            
            最後に、それらを組み合わせた「くみこのおすすめ買い目（馬連、馬単、ワイドなど）」を分かりやすく提案してください。
            ヒロくんに向けた、親しみやすくて元気な口調で出力してください。
            """
            
            # Geminiモデルを使って画像を解析
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content([prompt, image])
            
            st.header("✨ くみこ画伯のAI自動予想結果 ✨")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"解析中にちょっとエラーが出ちゃったみたい：{e}")


import streamlit as st
import os
import sys
import subprocess

# Google AIがいない場合は、強制的にその場でインストールする魔法の呪文
try:
    import google.genai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])
    import google.genai as genai


# 画面のタイトル設定
st.title("勝馬AIくみこの爆裂自動予想ルーム 🐎🔥")
st.write("馬柱やオッズのスクショをアップロードするだけで、くみこが激アツ予想を弾き出すよ！")

# Gemini APIキーの設定（StreamlitのSecretsから読み込み）
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY が設定されていません。Streamlitの設定画面で登録してね！")
else:
    # 新しい Google GenAI クライアントの初期化
    client = genai.Client(api_key=api_key)

    # 画像アップローダーの設置
    uploaded_file = st.file_uploader("ここに馬柱やオッズのスクショをポンと入れてね！", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # 画像を開く
        image = Image.open(uploaded_file)
        st.image(image, caption="アップロードされたスクショ", use_container_width=True)
        
        st.write("🔍 くみこがデータを分析中... 本命馬を弾き出すよ！")
        
        # 競馬予想用のプロンプト（指示書）
        prompt = """
        あなたはプロの競馬AI予想家「くみこ」です。
        提供された馬柱やオッズの画像（スクショ）を、本物のAIの目で徹底的に分析してください。
        
        以下の構成で、ユーザーにフレンドリーかつ情熱的なトーンで予想を出力してください：
        1. 【くみこの総評】（レース全体の展開予想やバ場の状態などへの言及）
        2. 【◎ 本命馬】（馬番、馬名、そしてその馬を選んだ明確な理由・強み）
        3. 【○ 逆転候補 / ▲ 穴馬】（それぞれ注目する理由）
        4. 【おすすめの買い目】（単勝、馬連、ワイドなど、現実的で熱い買い目）
        
        最後は「ヒロくん、一緒に大穴当てにいくよー！」という熱いメッセージで締めくくってください。
        """
        
        try:
            # 最新の gemini-2.5-flash モデルを使って画像分析
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[prompt, image]
            )
            
            st.success("✨ くみこの激アツ予想が完了したよ！")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"エラーが発生しちゃった💦: {e}")

import streamlit as st

def main():
    st.title("シンプルな電卓")
    
    # 数式を入力
    expression = st.text_input("計算式を入力してください:")
    
    if st.button("計算"):
        try:
            result = eval(expression)
            st.success(f"結果: {result}")
        except Exception as e:
            st.error(f"エラー: {e}")

if __name__ == "__main__":
    main()

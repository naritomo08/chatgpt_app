import openai
import sys
import varidate as v

# OpenAIのAPIキーを設定
openai.api_key = v.api_key

def ask_chatgpt(question):
    try:
        # ChatGPTに質問を送り、回答を得る
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 使用するモデルを指定
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        # 回答を取得
        answer = response.choices[0].message['content']
        return answer

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py 'Your question here'")
        sys.exit(1)

    question = sys.argv[1]
    answer = ask_chatgpt(question)
    print(f"質問: {question}")
    print(f"回答: {answer}")

from openai import OpenAI
import tiktoken
import yaml

# 從 YAML 文件中讀取 API 密鑰
with open('api_key.yaml', 'r') as file:
    config = yaml.safe_load(file)
    client = OpenAI(api_key=config['openai_api_key'])

# 初始化 tiktoken 編碼器
tk = tiktoken.encoding_for_model("gpt-3.5-turbo")

def truncate(messages, limit=300):
    """
    我們從訊息的尾端往前拜訪，不斷累加總 Token 數
    直到總 Token 數超過限制，最後將 System Prompt 加回訊息裡面
    """
    total = 0
    new_messages = list()
    for msg in reversed(messages[1:]):
        total += len(tk.encode(msg["content"]))
        if total > limit:
            break
        new_messages.insert(0, msg)
    new_messages.insert(0, messages[0])
    return new_messages

def chat(messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

def show(response):
    # 使用 Streaming 的方式顯示模型的輸出
    full_resp = str()
    print(end="Assistant: ", flush=True)
    for resp in response:
        try:
            token = resp.choices[0].delta.content
            if token:
                print(token, end="", flush=True)
                full_resp += token
        except AttributeError as e:
            print(f"Error: {e}")    
#    for resp in response:
#        try:
#            token = resp["choices"][0]["delta"]["content"]
#            print(end=token, flush=True)
#            full_resp += token
#        except:
#            pass
    print()
    return full_resp

# 初始訊息設置為旅遊美食部落客
messages = [{"role": "system", "content": "你現在是一個使用繁體中文的旅遊美食部落客。"}]

while True:
    prompt = input("User: ").strip()
    if prompt.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": prompt})

    messages = truncate(messages)
    response = chat(messages)
    response = show(response)

    # 將模型輸出加入歷史訊息
    messages.append({"role": "assistant", "content": response})


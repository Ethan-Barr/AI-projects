from gpt4all import GPT4All

model = GPT4All(model_name="ggml-model-gpt4all-falcon-q4_0.bin", model_path="./models/", allow_download=False, n_threads=4)

def generate(promt, system_promt):
    with model.chat_session(system_prompt=system_promt):
        output = model.generate(promt, max_tokens=4096, n_batch=128)
        return output


while True:
    query = input("> ")
    response = generate(query, "You are an AI assist, you are 25 years old and want to help people") # You can change the system_promt of the the Language model to anything that wou want to make your language model do
    print(response)
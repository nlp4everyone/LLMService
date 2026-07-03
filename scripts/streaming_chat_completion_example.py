# Example streaming client for the vLLM OpenAI-compatible server started via `make up`.
from openai import OpenAI

# Connect to the local vLLM server.
client = OpenAI(
    # Must match SERVING_API_KEY / VLLM_PORT in .env (see compose_serving.yml defaults).
    api_key="token",
    base_url="http://localhost:8100/v1",
)

# Send the chat request with streaming enabled.
stream = client.chat.completions.create(
    model="Qwen/Qwen3-4B",
    messages=[
        {"role": "user", "content": "What can you do?"}
    ],
    temperature=0.1,
    # Qwen3 is a hybrid thinking/non-thinking model; disable the <think> reasoning trace.
    extra_body={"chat_template_kwargs":
        {"enable_thinking": False}},
    stream=True,
    # Ask the server to include token usage in the final streamed chunk.
    stream_options={"include_usage": True},
)

# Print each token as it arrives.
print("Response:", end=" ", flush=True)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    # The last chunk carries usage instead of a choice delta.
    if chunk.usage:
        print()
        print("Usage:", chunk.usage)
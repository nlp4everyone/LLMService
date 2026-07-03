# Example client for the vLLM OpenAI-compatible server started via `make up`.
import time

from openai import OpenAI

# Connect to the local vLLM server.
client = OpenAI(
    # Must match SERVING_API_KEY / VLLM_PORT in .env (see compose_serving.yml defaults).
    api_key="token",
    base_url="http://localhost:8100/v1",
)

# Send the chat request, timing it to estimate throughput.
start_time = time.perf_counter()
response = client.chat.completions.create(
    model="Qwen/Qwen3-4B",
    messages=[
        {"role": "user", "content": "What can you do?"}
    ],
    temperature=0.1,
    # Qwen3 is a hybrid thinking/non-thinking model; disable the <think> reasoning trace.
    extra_body={"chat_template_kwargs":
        {"enable_thinking": False}}
)
elapsed_seconds = time.perf_counter() - start_time

# Print the model's reply.
print("Response:", response.choices[0].message.content)
# Print token usage (prompt/completion/total tokens).
print("Usage:", response.usage)
# Estimate output throughput (non-streaming, so this includes prompt processing time too).
print(f"Throughput: {response.usage.completion_tokens / elapsed_seconds:.2f} tokens/s")

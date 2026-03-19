"""Simple chatbot demo using an OpenAI-compatible API (e.g., DeepSeek / VolcEngine).

This script shows how to:
  - Read a question from stdin
  - Send it to a large language model via API
  - Print the model's reply

配置说明见 README。
"""

import os
import sys

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None


def call_openai(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Call an OpenAI-compatible API (OpenAI, DeepSeek, etc.)."""

    if openai is None:
        raise RuntimeError(
            "`openai` not installed. Run `pip install -r requirements.txt` and try again."
        )

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Please set OPENAI_API_KEY in your environment.")

    openai.api_key = api_key

    # If using a custom compatible endpoint (DeepSeek / VolcEngine), set OPENAI_API_BASE.
    base_url = os.environ.get("OPENAI_API_BASE")
    if base_url:
        openai.api_base = base_url

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=600,
    )

    return response.choices[0].message.content.strip()


def main():
    print("Chatbot demo (OpenAI-compatible API, e.g. DeepSeek)")
    print("Type a question and press Enter. Type 'quit' to exit.\n")

    while True:
        try:
            prompt = input("> ").strip()
            if not prompt:
                continue
            if prompt.lower() in {"quit", "exit", "q"}:
                print("Goodbye.")
                break

            answer = call_openai(prompt)

            print("\n=== Response ===")
            print(answer)
            print("===============\n")

        except KeyboardInterrupt:
            print("\nInterrupted. Bye.")
            break
        except Exception as err:
            print(f"Error: {err}\n")


if __name__ == "__main__":
    main()

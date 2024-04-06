import json
import requests


def chat(messages, model='tinydolphin', verbose=False):
    """Sends messages to a chat API and returns the response."""
    response = requests.post(
        "http://0.0.0.0:11434/api/chat",
        json={"model": model, "messages": messages, "stream": True},
    )
    response.raise_for_status()
    output = ""

    for line in response.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if not body.get("done"):
            content = body.get("message", {}).get("content", "")
            output += content
            if verbose:
                print(content, end="", flush=True)
        if body.get("done"):
            body["message"]["content"] = output
            return body["message"]

def embed(message, model='nomic-embed-text'):
    """Sends a message to an embedding API and returns the response."""
    url = "http://localhost:11434/api/embeddings"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json={"model": model, "prompt": message}, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"
    
def main():
    """Runs a CLI chat bot using a local model."""
    messages = []

    while True:
        user_input = input("Enter a prompt: ").strip()
        if not user_input:
            break
        messages.append({"role": "user", "content": user_input})
        response_message = chat(messages, verbose=True)
        messages.append(response_message)
        print("\n\n")

if __name__ == "__main__":
    main()

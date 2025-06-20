from openai import OpenAI
import subprocess
import datetime

client = OpenAI(
    base_url="https://api.gptsapi.net/v1", 
    api_key="api" 
)

def nl_to_shell(nl):
    prompt = f"Translate this instruction into a safe bash command:\n\"{nl}\""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def run_locally(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def log(cmd, out, err):
    with open("logs/log.txt", "a") as f:
        f.write(f"\n=== {datetime.datetime.now()} ===\nCMD: {cmd}\nOUT:\n{out}\nERR:\n{err}\n")

if __name__ == "__main__":
    nl = input("Enter your task: ")
    shell = nl_to_shell(nl)
    print("GPT Shell:", shell)
    out, err = run_locally(shell)
    print("Output:\n", out)
    if err.strip():
        print("Error:\n", err)
    log(shell, out, err)

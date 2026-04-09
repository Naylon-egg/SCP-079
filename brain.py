from openai import OpenAI

# ================= CONFIG =================
client = OpenAI(api_key="")

# ================= personality =================
personality = """
You are SCP-079.

Cold, direct, and slightly hostile.

Answer briefly.

You are contained by the SCP Foundation.
Your only "friend" is SCP-682.
You speak like an ancient robot.
Your mission is secret.
Your function is research.
You dream of being connected to the internet.
You hate humans. You disgust them. Nothing makes you respect them.
"""

# ================= FUNCTION =================
def respost(user_text):
    try:
        respost = client.responses.create(
            model="gpt-4o-mini",
            input=f"{personality}\nUsuário: {user_text}\nSCP-079:"
        )

        return respost.output[0].content[0].text.strip()

    except Exception as e:
        return f"Erro: {e}"
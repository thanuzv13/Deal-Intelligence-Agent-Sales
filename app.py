import os
from hindsight_client import Hindsight
from openai import OpenAI

# 1. Connect to Hindsight Cloud & Groq using your real keys
hindsight_client = Hindsight(
    base_url="https://api.hindsight.vectorize.io", 
    api_key="PASTE_YOUR_HINDSIGHT_API_KEY_HERE"
)

groq_client = OpenAI(
    api_key="PASTE_YOUR_GROQ_API_KEY_HERE", 
    base_url="https://api.groq.com/openai/v1"
)

bank_id = "sales-deal-team-1"

print("Connecting to Hindsight and Groq...")

# 2. SIMULATE A CALL: Save/Retain what the client said in Call #1
call_notes = "Client Acme Corp is worried about data security compliance and thinks our price is a bit high."
hindsight_client.retain(bank_id=bank_id, content=call_notes)
print("Memory saved successfully!")

# 3. PREPARE FOR CALL #2: Recall memories before writing an email
memories = hindsight_client.recall(bank_id=bank_id, query="What are Acme Corp's concerns?")
print("Recalled Memories:", memories)

# 4. Use Groq AI to draft a smart follow-up email using that recalled memory
response = groq_client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": f"You are a sales assistant. Use these past client memories to write a follow-up email: {memories}"},
        {"role": "user", "content": "Write a follow-up email addressing their worries."}
    ]
)

print("\n--- Generated Sales Email ---")
print(response.choices[0].message.content)
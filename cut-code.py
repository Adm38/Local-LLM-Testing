completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
)



message_log = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]
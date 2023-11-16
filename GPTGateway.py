import openai

api_key_1 = "<SECRET_KEY>"

class GPTGateway:
    @staticmethod
    def query(user_prompt, context = [], message_mode = "nocontext", mode="external", max_tok = 50, t = 0):
        openai.api_key = api_key_1
        
        prompt = [{"role": "user", "content": user_prompt}]
        if message_mode = 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature = t
        )
        print(response)
        return response.choices[0]["message"]["content"]

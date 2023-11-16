import openai

api_key_1 = "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"

class GPTGateway:
    @staticmethod
    def query(user_prompt, mode="external", max_tok = 50):
        openai.api_key = api_key_1
        
        prompt = [{"role": "user", "content": user_prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature = 0
        )
        print(response)
        return response.choices[0]["message"]["content"]

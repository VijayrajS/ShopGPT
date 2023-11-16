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

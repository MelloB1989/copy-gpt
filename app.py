from flask import Flask, request, send_file
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

@app.route('/generate-code', methods=['POST'])
def generate_code():
    prompt = request.json['prompt']
  
    # Generate code using OpenAI's GPT-3.5 model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
  
    code = response.choices[0].text.strip()
  
    # Write code to a file
    with open('generated_code.c', 'w') as file:
        file.write(code)
  
    return send_file('generated_code.c', as_attachment=True)

if __name__ == '__main__':
    app.run()

## Copy-GPT

Copy-GPT is a Flask-based web application that leverages OpenAI's GPT-3.5 model to generate C code based on user prompts. This documentation will guide you through the installation process and explain how to use the application.

### Prerequisites

Before installing and running Copy-GPT, ensure that you have the following prerequisites:

- Python 3.7 or higher installed on your system
- OpenAI API key

### Installation

To install and set up Copy-GPT, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/Copy-GPT.git
   ```

2. Change to the project directory:

   ```shell
   cd Copy-GPT
   ```

3. Create and activate a virtual environment (optional, but recommended):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Configuration

Before running the application, you need to configure your OpenAI API key. Follow these steps:

1. Open the `app.py` file in a text editor.

2. Locate the following line:

   ```python
   openai.api_key = 'YOUR_API_KEY'
   ```

3. Replace `'YOUR_API_KEY'` with your actual OpenAI API key.

### Usage

To use Copy-GPT and generate C code, follow these steps:

1. Start the Flask server:

   ```shell
   python app.py
   ```

2. Open a terminal or command prompt and use the following curl command to generate code:

   ```shell
   curl -X POST -H "Content-Type: application/json" -d '{"prompt":"Your prompt goes here"}' http://localhost:5000/generate-code --output generated_code.c
   ```

   Replace `"Your prompt goes here"` with your desired code prompt.

3. The generated C code will be downloaded and saved as `generated_code.c` in the current directory.

### Contributing

Contributions to Copy-GPT are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please open an issue or submit a pull request on the [GitHub repository](https://github.com/mellob1989/Copy-GPT).

### License

Copy-GPT is licensed under the [MIT License](LICENSE).

### Acknowledgments

Copy-GPT is built using OpenAI's GPT-3.5 model. We are grateful to OpenAI for providing the powerful language model.

### Support

If you need any assistance or have any questions, feel free to contact the project maintainer at mellob@noobslearning.com.

That's it! You now have Copy-GPT installed and running on your system. You can customize the documentation as needed, providing more details or adding specific instructions if required.

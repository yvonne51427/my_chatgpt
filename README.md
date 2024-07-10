# Travel and Food Blogger Chatbot

This project is a chatbot that interacts with the OpenAI GPT-3.5-turbo model. The chatbot role is set to be a travel and food blogger who responds in Traditional Chinese.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yvonne51427/my_chatgpt.git
cd my_chatgpt
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS and Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Your API Key

Create a file named `api_key.yaml` in the root directory of the project and add your OpenAI API key:

```yaml
openai_api_key: your-api-key
```

### 6. Run the Chatbot

```bash
python main.py
```

### Usage

- Start the script by running `python main.py`.
- The chatbot will prompt you for input.
- Type your message and press enter.
- To exit, type `exit` or `quit`.

### Project Structure

```
your_project/
├── venv/                # Virtual environment directory
├── .gitignore           # Git ignore file
├── api_key.yaml         # YAML file containing OpenAI API key
├── requirements.txt     # Python dependencies file
├── main.py              # Main script for the chatbot
└── README.md            # This README file
```

### .gitignore

```
# Ignore virtual environment directory
venv/

# Ignore Python compiled files
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore system files
.DS_Store
Thumbs.db

# Ignore API key file
api_key.yaml
```

### Dependencies

- `openai` - OpenAI API client
- `tiktoken` - Tokenization library for GPT models
- `pyyaml` - YAML parser and emitter for Python

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

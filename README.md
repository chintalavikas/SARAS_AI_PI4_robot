# SARAS AI PI4 Robot

An offline AI voice assistant robot built using Raspberry Pi 4, Python,Faster-Whisper , Ollama, TTS/STT, and animated HTML eyes.

---

## 🤖 AI & Software Stack

| Technology | Purpose |
|------------|----------|
| Faster-Whisper | Speech-to-Text (STT) |
| Piper TTS | Text-to-Speech (TTS) |
| Ollama + qwen2.5:0.5b | Offline AI Brain |
| Groq API + Llama 3 | Online AI Brain (Fast Responses) |
| Python 3 | Main Programming Language |
| Flask | Robot Eyes Web Interface |
| HTML/CSS/JavaScript | Animated Robot Eyes |
---

## Project Structure

```bash
SARAS_AI_PI4/
│
└── saras_ai/
    ├── saras_ai.py
    ├── eyes.html
    ├── style.css
    ├── script.js
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    │
    ├── modules/
    │   ├── stt.py
    │   ├── tts.py
    │   └── llm.py
    │   ├──  ultrasonic.py
    │   ├──  servo.py
    │   ├──  motors.py
    │   └──  eyes.py
    │
    │
    ├── images/
    ├── audio/
    └── models/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/chintalavikas/SARAS_AI_PI4_robot.git
```

## Install Requirements

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python saras_ai.py
```
### Installation commands

## Update Raspberry Pi

```bash
sudo apt update && sudo apt upgrade -y
```

---

# Install Python & Pip

```bash
sudo apt install python3 python3-pip -y
```

---

# Install Audio Dependencies

```bash
sudo apt install portaudio19-dev ffmpeg espeak-ng -y
```

---

# Install Ollama (LLM)

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## Run TinyLLaMA

```bash
ollama run tinyllama
```

## Run Deepseek-Coder

```bash
ollama run deepseek-coder:1.3b
```

---
# 🎤 Install STT (Faster-Whisper)

## Update System

```bash
sudo apt update
```

## Install Dependencies

```bash
sudo apt install python3-pip ffmpeg -y
```

## Install Faster-Whisper

```bash
pip install faster-whisper
```

## Verify Installation

```bash
python3 -c "from faster_whisper import WhisperModel; print('Faster-Whisper installed successfully!')"
```

---

# Install TTS (Coqui TTS)

```bash
pip install TTS
```

# 🌐 Install Online AI Brain (Groq + Llama 3)

## Install Groq Python SDK

```bash
pip install groq
```

## Get a Groq API Key

1. Create an account at Groq Cloud
2. Generate an API key
3. Store it securely

## Set API Key (Linux/Raspberry Pi)

```bash
export GROQ_API_KEY="your_api_key_here"
```

## Verify Installation

```python
from groq import Groq

client = Groq(api_key="your_api_key_here")

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response.choices[0].message.content)
```

---

## Additional Compatibility Packages

```bash
pip install bnnumerizer bnunicodenormalizer gruut[de,es,fr]==2
```

---

# Install Project Requirements

```bash
pip install -r requirements.txt
```

---

# Run SARAS AI

```bash
python saras_ai.py
```

---

# Note

Large AI models are not included in this repository.
Please download them manually using the commands above.
---

## AI Features

- Voice command recognition
- Local AI processing
- Robot eye animation
- Interactive assistant behavior
- Manual mode

---

## Robot Images

![alt text](<saras architecture.png>) ![alt text](<saras robot.png>)/



---

## Credits

This project was inspired by TechByAnand's AI assistant project.
I modified and customized several features for learning and experimentation.

---

## Author

Vikas Chinthala

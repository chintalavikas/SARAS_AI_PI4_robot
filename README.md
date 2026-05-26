# SARAS AI PI4 Robot

An offline AI voice assistant robot built using Raspberry Pi 4, Python, Vosk, Ollama, TTS/STT, and animated HTML eyes.

---

## Features

- Offline voice assistant
- Speech-to-Text (STT)
- Text-to-Speech (TTS)
- AI chatbot using LLM
- Animated robot eyes using HTML/CSS
- Raspberry Pi 4 support
- Voice interaction
- Modular Python architecture

---

## Technologies Used

- Python
- Raspberry Pi 4
- Vosk Speech Recognition
- Ollama
- HTML/CSS/JavaScript
- pyttsx3
- Flask

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
# Install STT (Vosk)

```bash
sudo apt update
```

```bash
sudo apt install python3-pip portaudio19-dev -y
```

```bash
pip install vosk sounddevice
```

---

# Install TTS (Coqui TTS)

```bash
pip install TTS
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
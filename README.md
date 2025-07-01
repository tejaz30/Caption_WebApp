---
# 🖼️ AI Image Captioning Web App

A Flask web application that generates intelligent captions for uploaded images using state-of-the-art Vision Transformer and GPT-2 models. Features a sleek, responsive interface with real-time caption generation and an image gallery.

---

## 🚀 Live Demo

🌐 **[Try it live on Hugging Face Spaces](https://huggingface.co/spaces/teja-bulusu/caption-webapp)**

---

## ✨ Features

- **🤖 AI-Powered Captioning** - Generates natural language descriptions for any image
- **🎨 Custom UI** - Beautiful, responsive HTML/CSS interface (no frameworks needed)
- **🖼️ Image Gallery** - View recently captioned images with their descriptions
- **⚡ Real-time Processing** - Instant caption generation upon upload
- **📱 Mobile Friendly** - Works seamlessly on desktop and mobile devices
- **🔄 Session Persistence** - Gallery maintains history during your session

---

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **AI Model**: `nlpconnect/vit-gpt2-image-captioning`
 - Vision Transformer (ViT) for image encoding
 - GPT-2 for natural language generation
- **Frontend**: Vanilla HTML5, CSS3, JavaScript
- **Image Processing**: PIL (Python Imaging Library)
- **Deep Learning**: PyTorch, Transformers

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/image-caption-webapp.git
   cd image-caption-webapp
   ```

2. **Create a Virtusal Environment**
    ```bash

    python -m venv venv

    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Application**
    ```bash
    python app.py
    ```

5. **Open your browser Navigate to http://localhost:7860**

---

## How It Works

- Upload Image - User selects and uploads an image through the web interface
- Image Processing - PIL converts the image to RGB format
- Feature Extraction - Vision Transformer extracts visual features
- Caption Generation - GPT-2 generates natural language description
- Display Results - Caption is displayed alongside the image
- Gallery Update - Image and caption are added to the session gallery

---

## Deployment

### Hugging Face Spaces

This app is deployed on Hugging Face Spaces. The deployment configuration includes:

- Automatic model caching in /tmp/ directories
- Optimized for serverless environments
- Public accessibility with no authentication required

### Local Deployment
For production deployment, consider:

- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up proper logging and monitoring
- Implementing file upload limits and validation
- Adding user authentication if needed


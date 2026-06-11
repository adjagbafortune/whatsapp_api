# WhatsApp API Backend (Django)

This repository contains a production-ready, modular Django API built for WhatsApp messaging automation. Originally designed for GPT, the system has been refactored to seamlessly leverage **Google Gemini AI**, utilizing a decoupled architecture that isolates AI operations from core webhook handling.

<img src="./img/index.png" alt="index.png/"> <br>
<img src="./img/admin.png" alt="admin.png/"> <br>

## Features
* **Modular Plugin System:** Add new chat commands on the fly by dropping scripts into the `plugins/` directory.
* **AI-Powered:** Seamlessly integrates with OpenAI's GPT for natural conversational fallbacks.
* **Role-Based Access Control:** Built-in validation for Admin-only commands and user blacklisting.
* **Media Handling:** Process incoming images, videos, audio, and documents.

## Architecture & Core Components

The codebase follows a strict separation of concerns to allow easy maintenance and scaling:

* **`api/whatsapp_api_handle.py`**: Manages incoming and outgoing WhatsApp webhooks, user contexts, and payload routing.
* **`api/ai_service.py`**: Dedicated wrapper for the Google Gemini API. Handles prompt optimization, system instructions, and token safety limits independently of the webhooks.
* **`api/plugins/`**: Directory for extending bot capabilities (e.g., custom automation, external database interactions) without modifying the main workflow.

## Setup & Installation

1. **Clone & Navigate:**
```bash
   git clone https://github.com/adjagbafortune/whatsapp_api.git
   cd Whatsapp_api

```

2. **Install Dependencies:**

```bash
   pip install -r requirements.txt

```

3. **Configuration:**
Create a `.env` file in the root directory:

Create a `.env` file in the root directory and configure your credentials securely:

```env
# Django settings
SECRET_KEY=your_django_secret_key
DEBUG=True

# WhatsApp API configuration
WHATSAPP_TOKEN=your_whatsapp_access_token
VERIFY_TOKEN=your_webhook_verification_token

# AI Service Configuration
GEMINI_API_KEY=your_google_gemini_api_key

```

4. **Database Migrations:**

```bash
   python manage.py migrate

```

## Creating Plugins

To add a command, create a Python file in `api/plugins/`:

```python
pluginInfo = {
    "command_name": "ping",
    "admin_privilege": False,
    "description": "Replies with pong.",
}

def handle_function(message):
    message.outgoing_text_message = "Pong!"
    message.send_message()

```

## 🛡️ License

This project is licensed under the [License MIT](LICENSE).

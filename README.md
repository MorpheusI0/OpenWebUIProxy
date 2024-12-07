# Open WebUI Proxy

This project is a Flask-based forward proxy that acts as a local instance of Ollama and forwards requests to a specified remote instance of Open WebUI with authentication. It is designed to be easily configurable and secure, using environment variables to manage sensitive information such as API keys.

## Why This Project is Necessary

Ollama typically runs locally and does not include authentication. Open WebUI is a browser-based UI built on top of Ollama, similar to ChatGPT, which enables user authentication and allows the generation of individual API keys for authentication. Many software components that offer Ollama integration do not support this authentication. Therefore, running this proxy is the simplest solution. In future this proxy could also be used for debugging and testing purposes.

## Configuration

The project uses environment variables to manage configuration settings. You can set these variables in a `.env` file. An example `.env` file is provided as `.env.example`.

### Environment Variables

- `OPEN_WEBUI_URL`: The base URL of the backend service.
- `API_KEY`: The API key to access the backend service.
- `HOST`: The host address for the Flask application (default is `127.0.0.1`).
- `PORT`: The port for the Flask application (default is `11434`).
- `DEBUG`: Enable or disable debug mode (default is `False`).

### Example `.env` File

```dotenv
OPEN_WEBUI_URL=https://<your-host.url>
API_KEY=sk-<your-api-key>
# HOST=127.0.0.1
# PORT=11434
# DEBUG=False
```

### Installation

1. Clone the repository:  
```
git clone git@github.com:MorpheusI0/OpenWebUIProxy.git
cd OpenWebUIProxy
```

2. Create a virtual environment and activate it:  
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:  
```
pip install -r requirements.txt
```

4. Create a `.env` file based on the [`.env.example`](.env.example) file and fill in your configuration details.  

### Running the Application
1. Activate the virtual environment:  
```
source venv/bin/activate
```

2. Run the application:  
```
python run.py
```

The application will start and listen on the specified host and port. You can now send requests to the proxy API, and it will forward them to the configured backend service.  

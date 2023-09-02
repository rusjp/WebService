# WebService :computer:

![GitHub](https://img.shields.io/github/license/rusjp/WebService) ![Python](https://img.shields.io/badge/python-3.x-blue)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

WebService is a web-based interface built with Flask for managing a single Linux service via `systemctl`. Start, stop, restart, and view the status of your chosen service remotely through a user-friendly dashboard.

## Installation

### Clone the repository
```bash
git clone https://github.com/rusjp/WebService.git
```

### Navigate to the project directory
```bash
cd WebService
```

### Install required packages
Make sure you have Python 3.x installed and then run:
```bash
pip install -r requirements.txt
```

### Configure Constants
Name the WebUI
```bash
APP_TITLE = 'Tailscale'
```

The Service to be restarted
```bash
SERVICE_NAME = 'tailscaled.service'
```

## Usage

1. **Start the Flask Application**
```bash
python app.py
```
The web interface should now be available at `http://localhost:80/`.

2. **Open the Dashboard**
   Open a web browser and navigate to the URL mentioned above.

3. **Control Your Service**
   Use the Start, Stop, and Restart buttons to control your chosen Linux service.


![WebService Screenshot](ui.png)

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Troubleshooting
If you encounter issues running the project, consider the following steps:

## ImportError or ModuleNotFoundError
Update Flask and its dependencies using pip install --upgrade Flask.
Reinstall itsdangerous with pip uninstall itsdangerous and pip install itsdangerous.
Script runs as sudo but not as user
Flask may be installed for a different user or environment. Try installing Flask as root using sudo pip install Flask.
Other Issues
## Ensure you have Python 3.x installed.
Make sure to activate the virtual environment if you're using one.
Check for multiple Python installations using which python3 and use the full path to run the script if necessary.
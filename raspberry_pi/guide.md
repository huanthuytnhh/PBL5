# Project Guide

**Important:** This project is designed to run **directly on a Raspberry Pi** to interact with connected hardware (GPIO pins, etc.). It will not function correctly on other systems like Windows or macOS.

This guide provides instructions on how to set up, run, and use this Raspberry Pi project.

## 1. Project Overview

This project controls hardware devices connected to a Raspberry Pi, potentially including LEDs and microphones, and may incorporate speech recognition capabilities.

**Key Components:**

- **`main.py`:** The main entry point for the application.
- **`control/`:** Contains modules for controlling hardware devices (e.g., `device_control.py`, `led_control.py`).
- **`speech/` (or `voice/`):** Contains modules related to speech processing or voice commands (e.g., `speech_recognition.py`).
- **`config.py` / `led_config.py`:** Configuration files for device settings (e.g., GPIO pins).
- **`logs/`:** Directory for storing log files.
- **`test_*.py`:** Scripts for testing individual components (e.g., `test_led.py`, `test_mic.py`).

## 2. Setup

### Prerequisites

- Raspberry Pi (with Raspberry Pi OS or similar)
- Python 3.x installed
- Required hardware connected (e.g., LEDs, microphone)
- Git (optional, for cloning the repository)

### Installation Steps

1.  **Clone the Repository (if applicable):**

    ```bash
    git clone <repository_url>
    cd raspberry_pi # Or your project directory name
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Linux/macOS
    # venv\Scripts\activate # On Windows
    ```

3.  **Install Dependencies:**
    Check for a `requirements.txt` file or review `setup.py`. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    # or if using setup.py for dependencies:
    # pip install .
    ```

    _(Note: If `requirements.txt` doesn't exist yet, you might need to manually install libraries mentioned in the code, like `RPi.GPIO`, speech recognition libraries, etc.)_

4.  **Configure Hardware Pins:**

    - Open the configuration files (e.g., `control/config.py`, `control/led_config.py`).
    - Verify that the GPIO pin numbers defined in the configuration match your hardware setup. Adjust if necessary.

5.  **Permissions (if needed):**
    - Ensure your user has the necessary permissions to access hardware interfaces like GPIO. You might need to add your user to the `gpio` group:
      ```bash
      sudo adduser $USER gpio
      ```
    - A reboot might be required after adding the user to the group.

## 3. Running the Project

1.  **Activate Virtual Environment (if used):**

    ```bash
    source venv/bin/activate # Or venv\Scripts\activate
    ```

2.  **Run the Main Script:**
    Execute the main application script:

    ```bash
    python main.py
    ```

3.  **Running Tests (Optional):**
    You can run individual test scripts to verify component functionality:
    ```bash
    python test_led.py
    python test_mic.py
    # etc.
    ```

## 4. Usage

- Describe how to interact with the project once it's running.
- If there's a command-line interface, explain the commands.
- If it responds to voice commands, provide examples.
- Explain what the LEDs indicate, if applicable.
- Refer to `logs/speech_log.txt` or other logs for output/debugging information.

## 5. Troubleshooting

- **GPIO Errors:** Double-check pin connections and configuration. Ensure correct permissions. Run `raspi-config` to enable necessary interfaces (like SPI, I2C if used).
- **Dependency Issues:** Make sure all required libraries are installed in the correct virtual environment.
- **Microphone Not Working:** Check microphone connections, ensure it's selected as the default input device in the OS audio settings, and verify necessary audio libraries are installed.
- **Check Logs:** Examine files in the `logs/` directory for error messages or clues.

---

_This guide should be updated as the project evolves._

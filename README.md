# PrimeEdge

PrimeEdge is a Python-based tool designed to enhance security by allowing advanced configuration of lock screen settings on Windows devices. It provides functionalities to customize the lock screen timeout, enable or disable fast user switching, and forcibly activate the lock screen.

## Features

- **Set Lock Screen Timeout**: Customize the timeout duration for the lock screen.
- **Enable/Disable Fast User Switching**: Control the fast user switching feature for added security.
- **Force Lock Screen**: Instantly activate the lock screen on demand.

## Requirements

- Windows Operating System
- Python 3.x
- Administrative privileges (required for registry modifications)

## Installation

Clone this repository to your local machine using:
```bash
git clone https://github.com/yourusername/PrimeEdge.git
```

## Usage

Run the program using Python:
```bash
python prime_edge.py
```

### Example

The example usage in the code sets the lock screen timeout to 10 minutes, disables fast user switching, and forces the lock screen to appear immediately.

```python
pe = PrimeEdge()
pe.set_lock_screen_timeout(600)  # Set timeout to 10 minutes
pe.enable_fast_user_switching(False)  # Disable fast user switching
pe.force_lock_screen()  # Force the lock screen to appear
```

## Disclaimer

This tool is intended for educational purposes and personal use. Use with caution, as modifying system settings can have unintended consequences. Ensure you have appropriate backups and permissions before using this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
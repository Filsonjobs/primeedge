import ctypes
import winreg

class PrimeEdge:
    def __init__(self):
        self.user32 = ctypes.windll.User32

    def set_lock_screen_timeout(self, timeout_seconds):
        """
        Set the lock screen timeout for Windows devices.
        :param timeout_seconds: Timeout in seconds
        """
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "ScreenSaveTimeOut", 0, winreg.REG_SZ, str(timeout_seconds))
            winreg.CloseKey(key)
            print(f"Lock screen timeout set to {timeout_seconds} seconds.")
        except Exception as e:
            print(f"Error setting lock screen timeout: {e}")

    def enable_fast_user_switching(self, enable=True):
        """
        Enable or disable fast user switching.
        :param enable: True to enable, False to disable
        """
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                 r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "HideFastUserSwitching", 0, winreg.REG_DWORD, 0 if enable else 1)
            winreg.CloseKey(key)
            status = "enabled" if enable else "disabled"
            print(f"Fast user switching {status}.")
        except Exception as e:
            print(f"Error setting fast user switching: {e}")

    def force_lock_screen(self):
        """
        Force the lock screen to appear immediately.
        """
        try:
            self.user32.LockWorkStation()
            print("Lock screen activated.")
        except Exception as e:
            print(f"Error activating lock screen: {e}")

# Example usage:
if __name__ == "__main__":
    pe = PrimeEdge()
    pe.set_lock_screen_timeout(600)  # Set timeout to 10 minutes
    pe.enable_fast_user_switching(False)  # Disable fast user switching
    pe.force_lock_screen()  # Force the lock screen to appear
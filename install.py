import os
import subprocess
import sys

GITHUB_REPO_URL = "https://github.com/yourusername/yourrepo.git"  # Replace with your repository URL

def install_default():
    print("\n[+] Installing WildFire (Default)...")
    
    # Clone the repository
    clone_repo()

    # Install dependencies
    install_dependencies()

    # Simulate additional installation steps
    print("[+] Default installation completed!")


def install_minimal():
    print("\n[+] Installing WildFire (Minimal)...")
    
    # Clone the repository
    clone_repo()

    # Simulate minimal installation (without dependencies, or only copying minimal files)
    print("[+] Minimal installation completed!")


def clone_repo():
    # Check if git is installed
    if shutil.which("git") is None:
        print("[!] Git is not installed. Please install Git and try again.")
        sys.exit(1)

    # Clone the repository
    if os.path.exists("wildfire"):
        print("[!] WildFire directory already exists. Skipping cloning.")
    else:
        try:
            subprocess.run(["git", "clone", GITHUB_REPO_URL, "wildfire"], check=True)
            print("[+] Repository cloned successfully!")
        except subprocess.CalledProcessError:
            print("[!] Failed to clone the repository.")
            sys.exit(1)


def install_dependencies():
    # Check if requirements.txt exists and install dependencies
    req_file = os.path.join("wildfire", "requirements.txt")
    if os.path.exists(req_file):
        print("[+] Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file])
    else:
        print("[!] No requirements.txt file found. Skipping dependency installation.")


def main_menu():
    print("Welcome to WildFire!")
    print("\nInstall a type:")
    print("[1] Default")
    print("[2] Minimal")
    print("[3] Exit")
    choice = input("\nTo choose default press enter, or type your choice: ")

    if choice == '1' or choice == '':
        install_default()
    elif choice == '2':
        install_minimal()
    elif choice == '3':
        print("\nExiting installer. Goodbye!")
        exit(0)
    else:
        print("\nInvalid choice. Please try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()

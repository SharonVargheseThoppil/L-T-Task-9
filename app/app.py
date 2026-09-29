import os
import socket
from datetime import datetime


def main():
    print("=" * 50)
    print("Docker Fundamentals Demo Application")
    print("=" * 50)

    print(f"Application started at: {datetime.now()}")
    print(f"Python version: {os.sys.version}")
    print(f"Container hostname: {socket.gethostname()}")

    print("\nEnvironment information:")
    print(f"Current working directory: {os.getcwd()}")

    print("\nDocker application is running successfully!")

    while True:
        print(f"Application heartbeat: {datetime.now()}")
        import time
        time.sleep(10)


if __name__ == "__main__":
    main()
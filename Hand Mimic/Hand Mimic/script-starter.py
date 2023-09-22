import subprocess

# Specify the script you want to run
script_to_run = "RockPaperScissors.py"

# Run the script and wait for it to finish
try:
    subprocess.run([r"C:/Users/WOB/AppData/Local/Programs/Python/Python311/python.exe", script_to_run], check=True, text=True, shell=True)
    print("Hello, World!")
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")

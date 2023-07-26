import argparse
import subprocess
import os
from colorama import init, Fore

def main():
    # Initialize colorama
    init()

    # Create a parser object
    parser = argparse.ArgumentParser(description='Validate .opt file with OperationalTemplateExtra.xsd schema using xmllint.')
    
    # Add an argument for the .opt file
    parser.add_argument('opt_file', type=str, nargs='?', help='The .opt file to validate.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # If no opt_file argument is provided, search the root directory for .opt files
    if args.opt_file is None:
        opt_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.opt')]
    else:
        opt_files = [args.opt_file]
    
    # Loop through the .opt files and validate each one
    for opt_file in opt_files:
        # Run the xmllint command
        command = f'xmllint --noout --schema OperationalTemplateExtra.xsd {opt_file}'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Print the output of the xmllint command
        if process.returncode != 0:
            print(f'{Fore.RED}Error validating {opt_file}:\n{stderr.decode()}{Fore.RESET}\n')
        else:
            print(f'{Fore.GREEN}Successfully validated {opt_file}.{Fore.RESET}\n')

if __name__ == '__main__':
    main()

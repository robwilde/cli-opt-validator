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
    
    # Add an argument for the log file
    parser.add_argument('--log', type=str, nargs='?', default=None, help='The file to log validation errors.')
    
    # Add an argument for the xsd file
    parser.add_argument('--xsd', type=str, nargs='?', default='OperationalTemplateExtra.xsd', help='The xsd file to use for validation.')
    
    # Parse the arguments
    args = parser.parse_args()

    # Initialize counters
    total_files = 0
    passed_files = 0
    failed_files = 0
    
    # If no opt_file argument is provided, search the templates directory for .opt files
    if args.opt_file is None:
        opt_files = [f for f in os.listdir('templates') if os.path.isfile(os.path.join('templates', f)) and f.endswith('.opt')]
    else:
        opt_files = [args.opt_file]
    
    # Loop through the .opt files and validate each one
    for opt_file in opt_files:
        # Run the xmllint command with the specified xsd file
        command = f'xmllint --noout --schema {args.xsd} {opt_file}'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Print the output of the xmllint command, log errors if necessary, and update counters
        total_files += 1
        if process.returncode != 0:
            error_message = f'{Fore.RED}Error validating {opt_file}:\n{stderr.decode()}{Fore.RESET}\n'
            print(error_message)
            failed_files += 1
            if args.log is not None:
                with open(args.log, 'a') as log_file:
                    log_file.write(error_message)
        else:
            print(f'{Fore.GREEN}Successfully validated {opt_file}.{Fore.RESET}\n')
            passed_files += 1

    # Print the counts of total, passed, and failed files
    print(f'Total files validated: {total_files}')
    print(f'Files passed validation: {passed_files}')
    print(f'Files failed validation: {failed_files}')

if __name__ == '__main__':
    main()

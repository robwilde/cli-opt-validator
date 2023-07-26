import argparse
import subprocess

def main():
    # Create a parser object
    parser = argparse.ArgumentParser(description='Validate .opt file with OperationalTemplateExtra.xsd schema using xmllint.')
    
    # Add an argument for the .opt file
    parser.add_argument('opt_file', type=str, help='The .opt file to validate.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the xmllint command
    command = f'xmllint --noout --schema OperationalTemplateExtra.xsd {args.opt_file}'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    # Print the output of the xmllint command
    if process.returncode != 0:
        print(f'Error validating {args.opt_file}:\n{stderr.decode()}')
    else:
        print(f'Successfully validated {args.opt_file}.')

if __name__ == '__main__':
    main()

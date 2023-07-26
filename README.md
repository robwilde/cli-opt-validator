# OPT Validator

This is a command-line application that validates .opt files against an xsd schema using xmllint.

## Installation

1. Clone the repository.
2. Install the dependencies by running `pip install -r requirements.txt`.

## Usage

Run the application with the command `python opt_validator.py`.

### Optional Parameters

- `--log`: Specify a file to log validation errors. If this option is not used, errors will only be printed to the console.
- `--xsd`: Specify a different xsd file to use for validation. If this option is not used, `OperationalTemplateExtra.xsd` will be used.

Example usage with optional parameters: `python opt_validator.py --log errors.log --xsd my_schema.xsd`

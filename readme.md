# Exist.io Integration for Home Assistant

This is a custom integration for Home Assistant that allows you to use Exist.io data within your Home Assistant setup. 

## Features

- Retrieve daily attributes from Exist.io including steps, sleep, productivity, and more.
- Use this data in your Home Assistant automations, scripts, or Lovelace UI.

## Requirements

- A Home Assistant installation running on the same network as this component.
- An Exist.io account with a valid token.

## Installation

1. Copy the repository into your `custom_components` directory. If you don't have a `custom_components` directory, you'll need to create one in the same directory as your `configuration.yaml` file.

2. Restart Home Assistant to load the component.

3. Go to Configuration > Integrations in the Home Assistant UI.

4. Click on the "Add Integration" button and search for "Exist.io".

5. Enter your Exist.io token in the text field and click "Submit".

To get an Exist.IO API Token, you must use [this code to generate a special simple auth token.](https://developer.exist.io/guide/read_client/#getting-a-token) 

## Usage

Once installed and configured, the Exist.io integration will create a sensor for each attribute available in your Exist.io account. You can use these sensors in your automations, scripts, or Lovelace UI just like any other sensor in Home Assistant.

## Troubleshooting

If you're experiencing issues with the Exist.io integration, please check the Home Assistant logs for any error messages. If you're still unable to resolve the issue, please open an issue on the GitHub repository.

## Contributing

Contributions to the Exist.io integration are welcome. Please open a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

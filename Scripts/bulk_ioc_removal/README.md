# Azure Threat Intelligence Bulk Indicator Removal

## Overview

This Python script is designed to facilitate the bulk removal of Azure Threat Intelligence Indicators from a Microsoft Sentinel workspace. It leverages Azure SDK for Python and Azure Identity Library for authentication.

## Requirements

- Python 3.6 or later
- Azure SDK for Python
- Azure Identity Library

## Installation

1. Install required Python packages:

   ```bash
   pip install azure-identity
   pip install requests
   ```

2. Ensure you have the necessary Azure credentials.

## Usage

```bash
python script_name.py -r <workspace_resource_group> -n <workspace_name> -s <subscription_id> -k <keyword>
```

### Parameters

- `-r, --workspace-rg`: Resource Group of the Microsoft Sentinel workspace.
- `-n, --workspace-name`: Name of the Microsoft Sentinel workspace.
- `-s, --subscription-id`: Azure Subscription ID.
- `-k, --keyword`: Keyword used to search for Indicators of Compromise (IoCs).

## Functionality

1. **Azure Threat Intelligence Indicator Retrieval**

   The script queries the Threat Intelligence Indicators in the specified Microsoft Sentinel workspace based on the provided keyword. It retrieves the indicators in batches of 100 entries until no more indicators are found.

2. **Indicator Deletion**

   For each retrieved indicator, the script attempts to delete it using the Azure Management API. Any errors during the deletion process are captured and reported.

3. **Output**

   The script provides information on the number of indicators processed during the execution.

## Example

```bash
python script_name.py -r MyResourceGroup \
                      -n MySentinelWorkspace \
                      -s abcdefgh-1234-5678-ijkl-9876543210ab \
                      -k malware
```

## Disclaimer

This script interacts with the Azure Management API to delete Threat Intelligence Indicators. Exercise caution to avoid unintentional data loss. Always review and understand the impact of the script before running it in a production environment.

## Author

[Your Name]

## License

This project is licensed under the [MIT License](LICENSE).

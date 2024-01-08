import argparse
import requests
from azure.identity import DefaultAzureCredential


def delete_indicator(indicator_id, indicator_value, token):
    try:
        url = f"https://management.azure.com{indicator_id}?api-version=2021-04-01"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        print(f"Deleted indicator: {indicator_id} - {indicator_value}")

    except requests.exceptions.HTTPError as err:
        print(f"Error deleting indicator {indicator_id}: {err}")


def get_az_threat_intelligence_indicators(
    workspace_rg, workspace_name, subscription_id, keyword
):
    try:
        # Get credentials and subscription ID
        credential = DefaultAzureCredential()
        workspace_id = f"/subscriptions/{subscription_id}/resourceGroups/{workspace_rg}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}"
        token = credential.get_token("https://management.azure.com/.default").token

        total_indicators = []
        length = 100

        # Get Indicators from Sentinel Threat Intelligence table
        # Keep fetching until nothing is found. The page size by default is 100 entries
        while length == 100:
            url = f"https://management.azure.com{workspace_id}/providers/Microsoft.SecurityInsights/ThreatIntelligence/main/queryIndicators?api-version=2021-04-01"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }
            payload = {"keywords": f"{keyword}"}

            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()

            indicators = response.json()["value"]
            total_indicators.append(indicators)

            for indicator in indicators:
                delete_indicator(
                    indicator["id"], indicator["properties"]["pattern"], token
                )

            length = len(indicators)
            print(f"Processed {len(indicators)} indicators")

        return total_indicators

    except requests.exceptions.HTTPError as err:
        print(f"Error getting Threat Intelligence Indicators: {err}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Azure Threat Intelligence Bulk Indicator Removal"
    )
    parser.add_argument(
        "-r", "--workspace-rg", required=True, help="Resource Group of the workspace"
    )
    parser.add_argument(
        "-n", "--workspace-name", required=True, help="Name of the workspace"
    )
    parser.add_argument(
        "-s", "--subscription-id", required=True, help="Azure Subscription ID"
    )
    parser.add_argument("-k", "--keyword", required=True, help="Keyword to search IoCs")

    args = parser.parse_args()

    indicators = get_az_threat_intelligence_indicators(
        args.workspace_rg, args.workspace_name, args.subscription_id, args.keyword
    )
    if indicators:
        if len(indicators) > 1:
            print(f"In total made {len(indicators)} queryIndicators searches")
        else:
            print(f"In total made {len(indicators)} queryIndicators search")


if __name__ == "__main__":
    main()

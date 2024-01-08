# Threat Intelligence Enrichment Playbooks for Azure Sentinel

This repository contains Azure Logic Apps and scripts designed to work with threat intelligence in Azure Sentinel. The SOAR playbooks integrate with the RST Cloud API, fetching detailed threat intelligence information for IP addresses, domains, URLs, and file hashes associated with security incidents.

## Playbook Descriptions

1. **Azure Logic App - Enrich multiple entities - RST IoC Lookup**

   - Automates the enrichment process using the RST Cloud API.
   - Separates processing for IP, URL, and hash entities for modular customisation.
   - Integrates enriched threat intelligence as comments in Azure Sentinel incidents.
   - [Learn More](LogicApps/rst-ioc-lookup/README.md)

2. **Azure Logic App - Enrich multiple entities - RST Noise Control**

   - (Brief description of the second playbook.)
   - (Key features and functionality.)
   - [Learn More](LogicApps/rst-ioc-lookup/README.md)

3. **Handy Script - (Script Name):**
   - (Description of the handy script included in the repository.)
   - (How the script enhances threat intelligence workflows.)
     [Learn More](Scripts/bulk_ioc_removal/README.md)

## Additional Resources

- [Using TI indicators in Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/use-threat-indicators-in-analytics-rules)
- [RST Cloud](https://www.rstcloud.com/)
- [RST IoC Lookup](https://www.rstcloud.com/rst-ioc-lookup/)
- [RST Noise Control](https://www.rstcloud.com/rst-noise-control/)

Feel free to explore, adapt, and contribute to enhance threat intelligence capabilities in your Azure Sentinel environment. For detailed information about each playbook and the handy script, refer to the respective links provided.

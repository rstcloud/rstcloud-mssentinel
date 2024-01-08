# Threat Intelligence Enrichment Playbooks for Microsoft Sentinel

This repository contains Azure Logic Apps and scripts designed to work with threat intelligence in Microsoft Sentinel. The SOAR playbooks integrate with the RST Cloud API, fetching detailed threat intelligence information for IP addresses, domains, URLs, and file hashes associated with security incidents.

## Content Descriptions

1. **Azure Logic App - Enrich multiple entities - RST IoC Lookup**

   - Gives an answer if an IP, Domain, URL, or Hash can be considered as malicious
   - Automates the enrichment process using the RST IoC Lookup.
   - Separates processing for IP, URL, and hash entities for modular customisation.
   - Integrates enriched threat intelligence as comments in Microsoft Sentinel incidents.
   - [Learn More](LogicApps/rst-ioc-lookup/README.md)

2. **Azure Logic App - Enrich multiple entities - RST Noise Control**

   - Gives an answer if an IP, Domain, URL, or Hash is a known-good or a very popular value that can be considered as noise
   - Automates the enrichment process using the RST Noise Control.
   - Separates processing for IP, URL, and hash entities for modular customisation.
   - Integrates enriched threat intelligence as comments in Microsoft Sentinel incidents.
   - [Learn More](LogicApps/rst-ioc-lookup/README.md)

3. **Script - Bulk IoC Removal**
   - bulk removal of IoCs from a Microsoft Sentinel workspace by search of a keyword.
     [Learn More](Scripts/bulk_ioc_removal/README.md)

## Additional Resources

- [Using TI indicators in Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/use-threat-indicators-in-analytics-rules)
- [RST Cloud](https://www.rstcloud.com/)
- [RST IoC Lookup](https://www.rstcloud.com/rst-ioc-lookup/)
- [RST Noise Control](https://www.rstcloud.com/rst-noise-control/)

Feel free to explore, adapt, and contribute to enhance threat intelligence capabilities in your Microsoft Sentinel environment. For detailed information about each playbook and the handy script, refer to the respective links provided.

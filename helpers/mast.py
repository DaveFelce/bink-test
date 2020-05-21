from collections import Counter
from typing import Dict, List


class MastHelper:
    """
    A helper class for all things to do with mast data
    """

    @staticmethod
    def list_by_current_rent(csv_rows: List) -> List:
        """
        Read in the CSV dataset file
        a. Produce a list sorted by "Current Rent" in ascending order
        b. Obtain the first 5 items from the resultant list and output to the console

        :param csv_rows: List of mast dataset records keyed on column headings
        :return: Sorted list of records by current rent
        """
        # Sort by Current Rent and take the top 5 records
        by_current_rent = sorted(csv_rows, key=lambda x: x["Current Rent"])[:5]

        return by_current_rent

    @staticmethod
    def list_by_lease_years(csv_rows: List) -> Dict:
        """
        From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
        a. Output the list to the console, including all data fields
        b. Output the total rent for all items in this list to the console

        :param csv_rows: List of mast dataset records keyed on column headings
        :return: Dict of a list of records matching the lease years and the total rent for this list
        """
        # Sort by Current Rent and take the top 5 records
        by_lease_years = list(filter(lambda x: x["Lease Years"] == 25, csv_rows))
        total_rent = 0
        for record in by_lease_years:
            total_rent += record["Current Rent"]

        return_val = {
           "by_lease_years": by_lease_years,
           "total_rent": total_rent
        }

        return return_val

    @staticmethod
    def count_of_masts(csv_rows: List) -> Dict:
        """
        Create a dictionary containing tenant name and a count of masts for each tenant
        a. Output the dictionary to the console in a readable form

        :param csv_rows: List of mast dataset records keyed on column headings
        :return: Dict of tenant names/masts for those tenants
        """

        mast_count = Counter()
        tenant_names = [x["Tenant Name"] for x in csv_rows]
        # Get a count of duplicate tenant names and therefore how many masts they have (assuming 1 record == 1 mast)
        for tenant_name in tenant_names:
            mast_count[tenant_name] += 1

        # Cast to dictionary
        mast_count = dict(mast_count)

        return mast_count


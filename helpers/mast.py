from typing import List


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
        :return:
        """
        # Sort by Current Rent and take the top 5 records
        by_current_rent = sorted(csv_rows, key=lambda x: x["Current Rent"])[:5]

        return by_current_rent

    @staticmethod
    def list_by_lease_years(csv_rows: List) -> List:
        """
        From the list of all mast data, create a new list of mast data with “Lease Years” = 25 years.
        a. Output the list to the console, including all data fields
        b. Output the total rent for all items in this list to the console
        :return:
        """
        # Sort by Current Rent and take the top 5 records
        by_lease_years = list(filter(lambda x: x["Lease Years"] == 25, csv_rows))

        return by_lease_years

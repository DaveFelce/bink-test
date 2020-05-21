import re

import arrow
from config import Config
from helpers.mast import MastHelper


class TestMastHelper:
    def test_list_by_current_rent(self, csv_rows):
        """
        Test the current rent listing meets the criteria:
        5 records sorted ASC on current rent
        """

        # GIVEN
        mast_helper = MastHelper()

        # WHEN
        # Returns only the top 5 in ASC order
        results = mast_helper.list_by_current_rent(csv_rows=csv_rows)
        first = results[0]["Current Rent"]
        last = results[4]["Current Rent"]

        # THEN
        assert len(results) == 5
        assert first <= results[2]["Current Rent"] <= last
        assert results[3]["Current Rent"] > results[2]["Current Rent"]
        assert results[4]["Current Rent"] > results[3]["Current Rent"]

    def test_list_by_lease_years(self, csv_rows):
        """
        Test the lease years listing meets the criteria:
        A list of mast data with “Lease Years” == 25 years.
        Output the total rent for all items in this list
        """

        # GIVEN
        mast_helper = MastHelper()

        # WHEN
        results = mast_helper.list_by_lease_years(csv_rows=csv_rows)
        by_lease_years = results["by_lease_years"]
        total_rent = results["total_rent"]

        # THEN
        assert len(by_lease_years) == 4
        assert by_lease_years[0]["Lease Years"] == 25
        assert by_lease_years[3]["Lease Years"] == 25
        assert total_rent == 46500.0

    def test_count_of_masts(self, csv_rows):
        """
        Test the lease years listing meets the criteria:
        Create a dictionary containing tenant name and a count of masts for each tenant
        """

        # GIVEN
        mast_helper = MastHelper()

        # WHEN
        results = mast_helper.count_of_masts(csv_rows=csv_rows)

        # THEN
        assert results["Arqiva Services ltd"] == 2
        assert results["Vodafone Ltd"] == 2
        assert results["O2 (UK) Ltd"] == 1
        assert results["Hutchinson3G Uk Ltd&Everything Everywhere Ltd"] == 1

    def test_list_by_lease_start_date(self, csv_rows):
        """
        Test that listing by lease start dates meet the criteria:
        List the data for rentals with "Lease Start Date" between 1st June 1999 and 31st August 2007
        with dates formatted as DD/MM/YYYY
        """

        # GIVEN
        mast_helper = MastHelper()
        low_date = arrow.get(Config.LOW_DATE, Config.DATASET_DATE_FORMAT)
        high_date = arrow.get(Config.HIGH_DATE, Config.DATASET_DATE_FORMAT)

        # WHEN
        results = mast_helper.list_by_lease_start_date(
            csv_rows=csv_rows, low_date=low_date, high_date=high_date
        )
        # Are the dates in the correct format?
        required_date_format = re.compile(r"^\d{2}[/]\d{2}[/]\d{4}$")

        # THEN
        assert len(results) == 4
        assert required_date_format.search(results[0]["Lease Start Date"])
        assert required_date_format.search(results[0]["Lease End Date"])
        assert required_date_format.search(results[3]["Lease Start Date"])
        assert required_date_format.search(results[3]["Lease End Date"])

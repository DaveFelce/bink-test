from helpers.mast import MastHelper


class TestMastHelper:
    def test_list_by_current_rent(self, csv_rows):
        """
        Test the current rent listing meets the criteria
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
        """

        # GIVEN
        mast_helper = MastHelper()

        # WHEN
        results = mast_helper.list_by_lease_years(csv_rows=csv_rows)

        # THEN
        assert len(results) == 4
        assert results[0]["Lease Years"] == 25
        assert results[3]["Lease Years"] == 25

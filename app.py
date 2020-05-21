import argparse
import pprint

from config import Config
from helpers.mast import MastHelper
from services.files import FileService


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        choices=["1", "2", "3", "4"],
        help="Please choose actions from 1 to 4, corresponding to the test criteria",
    )
    args = parser.parse_args()

    file_service = FileService()
    mast_helper = MastHelper()
    results = None
    # Load the dataset to work on
    csv_rows = file_service.get_csv_rows(csv_filepath=Config.DATASET_CSV)
    if args.action == "1":
        results = mast_helper.list_by_current_rent(csv_rows=csv_rows)
    if args.action == "2":
        results = mast_helper.list_by_lease_years(csv_rows=csv_rows)
    if args.action == "3":
        results = mast_helper.count_of_masts(csv_rows=csv_rows)

    pprint.pprint(results)


if __name__ == "__main__":
    main()

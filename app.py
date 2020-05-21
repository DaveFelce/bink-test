import argparse
import pprint

import arrow
import utils
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

    logger = utils.get_logger(__name__)
    file_service = FileService()
    mast_helper = MastHelper()
    results = None
    # Load the dataset to work on
    csv_rows = file_service.get_csv_rows(csv_filepath=Config.DATASET_CSV)

    try:
        if args.action == "1":
            results = mast_helper.list_by_current_rent(csv_rows=csv_rows)
        if args.action == "2":
            results = mast_helper.list_by_lease_years(csv_rows=csv_rows)
        if args.action == "3":
            results = mast_helper.count_of_masts(csv_rows=csv_rows)
        if args.action == "4":
            low_date = arrow.get(Config.LOW_DATE, Config.DATASET_DATE_FORMAT)
            high_date = arrow.get(Config.HIGH_DATE, Config.DATASET_DATE_FORMAT)
            results = mast_helper.list_by_lease_start_date(
                csv_rows=csv_rows, low_date=low_date, high_date=high_date
            )
    except Exception as e:
        logger.exception(e)

    pprint.pprint(results)


if __name__ == "__main__":
    main()

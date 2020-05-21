import argparse
import pprint

from config import Config
from services.files import FileService


def list_by_current_rent():
    """
    Read in the CSV dataset file
    a. Produce a list sorted by "Current Rent" in ascending order
    b. Obtain the first 5 items from the resultant list and output to the console
    :return:
    """
    file_service = FileService()
    csv_rows = file_service.get_csv_rows(csv_filepath=Config.DATASET_CSV)
    # Sort by Current Rent and take the top 5 records
    by_current_rent = sorted(csv_rows, key=lambda x: x["Current Rent"])[:5]

    return by_current_rent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        choices=["1", "2", "3", "4"],
        help="Please choose actions from 1 to 4, corresponding to the test criteria",
    )
    args = parser.parse_args()

    results = None
    if args.action == "1":
        results = list_by_current_rent()

    pprint.pprint(results)


if __name__ == "__main__":
    main()

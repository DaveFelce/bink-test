from typing import Dict, List

import pandas
import utils


class FileService:
    def __init__(self):
        self.logger = utils.get_logger(__name__)

    def get_csv_rows(self, csv_filepath: str) -> List[Dict]:
        """
        Process CSV file, turning each row into a dict keyed on fieldname

        :param csv_filepath: Path to CSV file
        :return: list of dicts, where each dict is a row from the file keyed on fieldnames (col headings)
        """
        data = pandas.read_csv(
            csv_filepath,
            sep=",",
            quotechar='"',  # single quote allowed as quote character
            keep_default_na=False,  # Keep empty strings as strings, not NaN
        )

        csv_rows = []
        fieldnames = data.columns.to_list()
        for row in data.values:
            row_as_dict = dict(zip(fieldnames, row.tolist()))
            csv_rows.append(row_as_dict)

        return csv_rows

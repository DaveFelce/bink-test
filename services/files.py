import csv
import re
from typing import Dict, List, Union

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
            # dtype={
            #     "year_group": int,
            #     "enrolment_id": str,
            #     "mobile_number": str,
            #     "programme_hierarchy": str,
            # },
            keep_default_na=False,  # Keep empty strings as strings, not NaN
        )

        csv_rows = []
        fieldnames = data.columns.to_list()
        for row in data.values:
            row_as_dict = dict(zip(fieldnames, row.tolist()))
            # row_as_dict["programme_hierarchy"] = self._process_programme_hierarchy(
            #     row_as_dict["programme_hierarchy"]
            # )
            csv_rows.append(row_as_dict)

        return csv_rows

    def _process_programme_hierarchy(
        self, programme_hierarchy: str
    ) -> Union[str, List]:
        """
        If programme hierarchy contains any strings, split it on '|' (which will always give an array even if there's
        only a single string). If it's an empty string, return an empty array.

        :param programme_hierarchy: Possibly | delimited string to be split
        :return:
        """
        if programme_hierarchy:
            programme_hierarchy = programme_hierarchy.split("|")
        else:
            programme_hierarchy = []

        return programme_hierarchy

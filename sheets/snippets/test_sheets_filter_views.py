"""
Copyright 2022 Google LLC
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest
import sheets_filter_views
from base_test import BaseTest


class Testfilterviews(BaseTest):
    """Unit test for sheets conditional_formatting value Sheet snippet"""

    def test_filter_views(self):
        """test filter view function"""
        spreadsheet_id = self.create_test_spreadsheet()
        self.populate_values(spreadsheet_id)
        sheets_filter_views.filter_views(spreadsheet_id)


if __name__ == "__main__":
    unittest.main()

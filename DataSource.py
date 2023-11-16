import json

class MockoDB:
    def __init__(self) -> None:
        self.product_info = {}
        self.summary_data = {}

        with open('review_summaries.json', 'r') as f:
            self.summary_data = json.load(f)

        with open('sim_list_info_1.json', 'r') as fp:
            self.product_info = json.load(fp)

    def get_summary(self, asin):
        return self.summary_data[asin]

    def get_product_info(self, asin):
        return self.product_info[asin]

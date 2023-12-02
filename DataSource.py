import json

class MockoDB:
    def __init__(self) -> None:
        self.product_info = {}
        self.summary_data = {}

        with open('review_summaries.json', 'r') as f:
            self.summary_data = json.load(f)

        with open('sim_list_info_1.json', 'r') as fp:
            self.product_info = json.load(fp)
        
        with open('tag_counts.json', 'r') as fp:
            self.tag_counts = json.load(fp)

    def get_summary(self, asin):
        return self.summary_data[asin]

    def get_product_info(self, asin):
        return self.product_info[asin]

    def get_tag_counts(self, asin):
        return self.tag_counts[asin]
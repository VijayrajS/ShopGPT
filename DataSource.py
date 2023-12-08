import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MockoDB:
    def __init__(self) -> None:
        self.product_info = {}
        self.summary_data = {}
        PYMONGO_URI = "mongodb+srv://shopgpt-beauty:3bbBVIYAcgnnqaln@beauty-review-cluster.em3e1lu.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(uri)
        self.db = client['shopgpt-beauty']

        with open('review_summaries.json', 'r') as f:
            self.summary_data = json.load(f)

        with open('sim_list_info_1.json', 'r') as fp:
            self.product_info = json.load(fp)
        
        with open('tag_counts.json', 'r') as fp:
            self.tag_counts = json.load(fp)
        
        with open('inv_ind.json', 'r') as fp:
            self.inv_ind = json.load(fp)
        
        with open('B00I11N2VO.json', 'r') as fp:
            self.B00I11N2VO_reviews = json.load(fp)

    def get_summary(self, asin):
        collection = db['general_summaries']
        summaries = collection.find({})
        return summaries

    def get_product_info(self, asin):
        summaries = collection.find({"asin":asin})
        return summaries

    def get_tag_counts(self, asin):
        summaries = collection.find({"asin":asin})
        return summaries

    def get_review_inv_ind(self, asin):
        return self.inv_ind[asin]

    def get_B00I11N2VO1_reviews(self):
        self.summaries = collection.find({"asin":"B00I11N2VO1"})
        return self.summaries

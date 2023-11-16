from GPTGateway import GPTGateway
import queries
import json
from collections import deque
from DataSource import MockoDB

class GPTService:
    def __init__(self) -> None:
        self.dbInstance = MockoDB()
        self.context = []
        self.product_context = set()
        #! WE NEED TO HAVE A CACHE FOR PRODUCT SUMMARIES

    def getQueryType(self, query):
        query_type_json = GPTGateway.query(queries.QUERY_TYPE_CLASSIFIER.format(query), mode = "internal")
        query_type_data = json.loads(query_type_json)
        
        return query_type_data

    def serve_query(self, query):
        self.context.append({"role": "user", "content": query})
        query_type_json = self.getQueryType(query)
        print(query_type_json)
        products = query_type_json["products"]
        self.product_context.add([p for p in products if p != "_related_"])
        query_type = query_type_json["type"]

        if query_type == "summary":
            if query_type_json["isRecent"]:
                return self.dbInstance.latest_summaries(products[0])
            else:
                response = "About " + products[0] + '\n'
                summary = self.dbInstance.get_summary(products[0])
                for key in summary.keys():
                    if key == "Net Rating":
                        rating = summary[key]
                        stars = int(rating)*'★' + ((rating - int(rating)) >= 0.5)*"½"
 
                        response += '''<p style='font-size: 20px;'><b>''' + key + '</b>' + ': ' + str(rating) + ' ' + stars + '</p><br/>'
                    else:
                        response += '''<p style='font-size: 20px;'><b>''' + key + '</b>' + ':<br/>' + str(summary[key]) + '</p><br/>'
                return response

        elif query_type == "comparision":
            if "_related_" in products:
                products.remove("_related_")
                products = list(set(products + list(self.product_context)))
            
            product_info_list = []
            product_summary_list = []

            for product in products:
                product_summary_list.append(self.dbInstance.get_summary(product))
                product_info_list.append(self.dbInstance.get_product_info(product))

            GPTGateway.query(queries.PRODUCT_COMPARISON_QUERY_SHORT.format(str(product_info_list), str(product_summary_list)))

        elif query_type == "suggestion":
            pass
        else:
            return GPTGateway.query(query)

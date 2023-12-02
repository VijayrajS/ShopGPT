from GPTGateway import GPTGateway
import queries
import json
from collections import defaultdict
from DataSource import MockoDB

class GPTService:
    def __init__(self) -> None:
        self.dbInstance = MockoDB()
        self.context = []
        self.product_context = set()
        self.summary_keyword_mode = False
        self.prev_summary_prod = ""

    def getQueryType(self, query):
        query_type_json = GPTGateway.query(queries.QUERY_TYPE_CLASSIFIER.format(query), mode = "internal")
        query_type_data = json.loads(query_type_json)
        
        return query_type_data

    def serve_query(self, query):
        print("Here")
        if self.summary_keyword_mode and query[0] == ":":
            
            return "It's working"
        
        self.context.append({"role": "user", "content": query})
        query_type_json = self.getQueryType(query)
        products = query_type_json["products"]
        self.product_context = self.product_context.union(set([p for p in products if p != "_related_"]))
        query_type = query_type_json["type"]

        if query_type == "summary":
            if "_related_" in products:
                products.remove("_related_")
            
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
                
                self.context.append({"role": "agent", "content": summary})
                self.summary_keyword_mode = True
                self.prev_summary_prod = products[0]
                
                keywords = self.dbInstance.get_tag_counts(products[0])
                print(keywords)
                top_keywords = sorted(keywords.keys(), key = lambda x: -keywords[x]["total"])[:min(len(keywords), 10)]
                def color_txt(txt, color):
                    return '''<div style="color: {};">'''.format(color) + txt + '''</div>'''
                
                response += '\n'
                
                top_keywords = [color_txt(keyw, 'green')
                                if defaultdict(int, keywords[keyw])['negative'] < defaultdict(int, keywords[keyw])['positive'] \
                                else color_txt(keyw, 'red') \
                                for keyw in top_keywords]
                
                response += ', '.join(top_keywords)
                return response

        elif query_type == "comparison":
            if "_related_" in products:
                products.remove("_related_")
                products = list(set(products + list(self.product_context)))
            
            if products == []:
                products = list(self.product_context)
            
            product_info_list = {}
            product_summary_list = {}
            print('Products: ', products)

            for product in products:
                product_summary_list[product] = self.dbInstance.get_summary(product)
                product_info_list[product] = self.dbInstance.get_product_info(product)
            print(product_info_list)
            print(product_summary_list)

            data_recommendation = {}
            for u in product_info_list.keys():
                x = product_info_list[u]
                x['reviews'] = ' '.join([str(_) for _ in list(product_summary_list[u].values())])
                data_recommendation[u] = x
            
            print('**')
            print('data rec:', data_recommendation)
            print('**')

            response = GPTGateway.query(queries.PRODUCT_COMPARISON_QUERY_FINAL.format(json.dumps(data_recommendation)), t = 0.8)
            self.context.append({"role": "agent", "content": response})
            return response

        elif query_type == "suggestion":
            if "_related_" in products:
                products.remove("_related_")
                products = list(set(products + list(self.product_context)))
            
            if products == []:
                products = list(self.product_context)
                
            print('Products: ', products)
            
            
            product_info_list = {}
            product_summary_list = {}

            for product in products:
                product_summary_list[product] = self.dbInstance.get_summary(product)
                product_info_list[product] = self.dbInstance.get_product_info(product)
            print(product_info_list)
            print(product_summary_list)
            data_recommendation = {}
            for u in product_info_list.keys():
                x = product_info_list[u]
                x['reviews'] = ' '.join([str(_) for _ in list(product_summary_list[u].values())])
                data_recommendation[u] = x
            
            print('**')
            print('data rec:', data_recommendation)
            print('**')

            response = GPTGateway.query(queries.RECOMMEND_QUERY.format(json.dumps(data_recommendation)), t = 0.5)
            print('reco response: ', response)
            self.context.append({"role": "agent", "content": response})
            return response
            
        else:
            return GPTGateway.query(query, context = self.context, mode = "context")

from django.conf import settings

class AmazonAffiliateMiddleware(object):
    
    def __init__(self):
        self.affiliate_code = 'jaymzcd'
        
    def process_response(self, request, response):
        
        return response

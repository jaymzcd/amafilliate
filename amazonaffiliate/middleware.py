from django.conf import settings
import re

class AmazonAffiliateMiddleware(object):
    
    def __init__(self):
        self.affiliate_code = 'jaymzcd'
        
    def process_response(self, request, response):
        response.content = re.sub(r'(amazon.co(m|.uk)/[/\w-]+)', r'\1%s' % \
            self.affiliate_code, response.content)
        return response

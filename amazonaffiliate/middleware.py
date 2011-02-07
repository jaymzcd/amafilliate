from django.conf import settings
from amazonaffiliate.exceptions import AmazonAffiliateException
import re

class AmazonAffiliateMiddleware(object):
    
    def __init__(self):
        try:
            self.affiliate_code = settings.AFFILIATE_USER
        except AttributeError:
            if settings.DEBUG:
                raise AmazonAffiliateException('No Affiliate User defined in settings.py')
            else:
                pass
        
    def process_response(self, request, response):
        response.content = re.sub(r'(amazon.co(m|.uk)/[/\w-]+)', r'\1%s' % \
            self.affiliate_code, response.content)
        return response

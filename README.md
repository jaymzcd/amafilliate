# Amazon Affiliate Middleware for Django

This is just a basic middleware/decorator pair to put in amazon affiliate
links from a setting variable. I get the feeling I could change it a bit to
replace links for a few more services. It's all pretty much the same thing.

## Config

Add to your `settings.py` file middleware tuple:

    ('amazonaffiliate.middleware.AmazonAffiliateMiddleware'),


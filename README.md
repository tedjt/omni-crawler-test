# LinkedIn Job spider interview test
Set up intro

1. Clone the repository `git clone git@github.com:tedjt/omni-crawler-test` on the host machine
2. `cd omni-crawler-test` on the host machine
2. `./setup.sh` to create, activate and configure a python virtualenv.
 - Read more at http://docs.python-guide.org/en/latest/dev/virtualenvs/.
3. Run spider with `scrapy runspider lawjobsspider.py`

Your goal for this test is to implement the logic for SimplyLawJobs.
The spider should navigate to the start_url, paginate through
the search results pages and visit each job listed.
For every job details page found, should produce a JobItem
with the relevant fields populated.

For pagination, you can use the Rule/LinkExtractor system for CrawSpider (the base class)
or you can manually paginate in the "parse" method that is called
after the first page of search results is loaded from the start_url.

There are some utilities defined in the file like `NormalizedJoin` and `JobItemLoader`
to help making generating clean item data easier.

## Some helpful resources

1. CrawlSpider documentation
 - http://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider
 - Example using Link extraction. http://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider-example
2. ItemLoader documentation
 - http://doc.scrapy.org/en/latest/topics/loaders.html
 - ItemLoaders produce an Item after transforming through input and output processors
 since a single xpath expression may contain many elements transformation is useful for processes
 like stripping tags, joining text together and removing whitespace.

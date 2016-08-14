from urlparse import urljoin, urlparse

import re
from scrapy import Request
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders.crawl import CrawlSpider
from scrapylib.processors import default_input_processor, default_output_processor


__author__ = 'ttomlins'


class NormalizedJoin(object):
    """ Strips non-empty values and joins them with the given separator. """

    def __init__(self, separator=u' ', return_list=False):
        self.separator = separator
        self.return_list = return_list

    def __call__(self, values):
        result = self.separator.join(
            [value.strip() for value in values if value and not value.isspace()])
        if self.return_list:
            return [result]
        else:
            return result


class JobItem(Item):
    # required fields
    title = Field()
    # a unique id for the job on the crawled site.
    job_id = Field()
    # the url the job was crawled from
    url = Field()
    # name of the company where the job is.
    company = Field()

    # location of the job.
    # should ideally include city, state and country.
    # postal code if available.
    # does not need to include street information
    location = Field()
    description = Field()

    # the url users should be sent to for viewing the job. Sometimes
    # the "url" field requires a cookie to be set and this "apply_url" field will be differnt
    # since it requires no cookie or session state.
    apply_url = Field()

    # optional fields
    industry = Field()
    baseSalary = Field()
    benefits = Field()
    requirements = Field()
    skills = Field()
    work_hours = Field()


class JobItemLoader(ItemLoader):
    default_item_class = JobItem
    default_input_processor = default_input_processor
    default_output_processor = default_output_processor
    # all text fields are joined.
    description_in = Identity()
    description_out = NormalizedJoin()
    requirements_in = Identity()
    requirements_out = NormalizedJoin()
    skills_in = Identity()
    skills_out = NormalizedJoin()
    benefits_in = Identity()
    benefits_out = NormalizedJoin()


REF_REGEX = re.compile(r'\/(\d+)$')

APPEND_GB = lambda x: x.strip() + ", GB"


class SimplyLawJobs(CrawlSpider):
    """ Should navigate to the start_url, paginate through
    the search results pages and visit each job listed.
    For every job details page found, should produce a JobItem
    with the relevant fields populated.

    You can use the Rule system for CrawSpider (the base class)
    or you can manually paginate in the "parse" method that is called
    after the first page of search results is loaded from the start_url.

    There are some utilities above like "NormalizedJoin" and JobItemLoader
    to help making generating clean item data easier.
    """
    start_urls = ["http://www.simplylawjobs.com/jobs"]
    name = 'lawjobsspider'

    #----------------#
    #----------------#
    #-YOUR CODE HERE-#
    #----------------#
    #----------------#



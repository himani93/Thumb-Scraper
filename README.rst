
Solution to Thumb Scraper
----


Assumptions:
---

2. All other urls are relative to base url specified at time of initialization
3. Default base URL is http://yolaw-tokeep-hiring-env.herokuapp.com
4. Pages is a valid json file
1. All the content to be scraped is of type `text/html`.
1. encoding of content is of `utf-8`
3. Scarping of content stops in following scenarios:
   a. URL of document to be retrieved is invalid.
   a. Documents could not be retrieved.
   b. Document cannot be parsed.
   c. `pages.json` json is invalid.
   d. A page in `pages.json` does not follow specified format.
   e. Next page is not found.


Questions:
---

1. Should a message be shown in case scraping stops due to one of the above mentioned reasons? If yes, what?
2. After how many iterations should the scraper stop?

Usage
---
1. Create a virtualenv and activate it.
2. `tar -xf tar -xf ThumbScraper-0.1.tar.gz`
3. `cd ThumbScraper-0.1`
4. `python setup.py install`
5. `thumbscraper --pages ./thumb_scarper/pages.json --url https://yolaw-tokeep-hiring-env.herokuapp.com/`

**Note** - Check `thumbscraper --help` for more info on params.

How to edit config:
---
1. Edit username and password in `ThumbScraper-0.1/thumb_scraper/config.py`
   ```
   USERNAME=<usernmae>  # default Thumb
   PASSWORD=<password>  # default Scraper
   ```

How to run tests:
---
1. `pip install -r test_requirements.txt`

2. `python setup.py test`

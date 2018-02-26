
Solution to Legalstart Thumb Scraper
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

Should a message be shown in case scraping stops due to one of the above mentioned reasons? If yes, what?


Usage
---
1. Create a virtualenv and activate it.
2. `pip install -r requirements.txt -r test_requirements.txt`
3. Create a `config.py` file in thumb_parser where authentication keys are provided.

   ```
   USERNAME=<usernmae>
   PASSWORD=<password>
   ```
4. `pip install -e .`
4.
   `thumbscraper --pages ./thumb_scarper/pages.json --url https://yolaw-tokeep-hiring-env.herokuapp.com/`

How to run tests:
---
`python setup.py test`

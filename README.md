# A crawer to get best selling products from Yahoo Buy (https://tw.buy.yahoo.com)

## Purpose
- to write a crawer to get best selling products from Yahoo Buy
- to write a query tool that is able to perform some options on crawled result

## Crawling Stragety
  after taking time to explore the site, there is a site map (https://tw.buy.yahoo.com/help/helper.asp?p=sitemap&hpp=sitemap) 
that we can use to  get all category (with query pattern /?z= ) and sub category ids (with query pattern /?sub=)

  By investigating category and sub category page, we can find a section 
called 熱門精選 at right side of the page.  The corresponding html id for this 
section is "cl-hotrank".  As the id name suggested (hotrank), I will simply 
assume the item listed here would be highly correlated to best selling products 

  At this point, what we need to do for this crawler would be: 
1. visitng all category and sub category pages 
2. getting all item's url in section with id equals 'cl-hotrank', 
3. collecting item information from each item's url 
4. saving item information in a excel or csv file for offline query


## Limitation
- because there is no way to get the information in terms of actual revenue or 
the quantity the product sold, it relys on the web site to put real HOT ITEMS
here.  
- although for each individual item page, there is a section called 本分類熱銷榜
(with id = 'cl-ordrank'), I didn't take it for consideration because those are 
items within sub sub category.  If we also take sub sub category result
into consideration in addition to catgoery and sub category, we might get too
many best selling products.  That might violate the meaning of best selling
products (if too many best selling products, the what do best selling products
mean?)

## Usage (yb.py)
### python version
3.6
### Required external modules
see used_modules.txt
### Directory structure
#### output
directory to save crawled result
#### lib
directory for python lib used for yb.py

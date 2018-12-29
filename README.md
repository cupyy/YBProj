# A crawer to get best selling products from Yahoo Buy (https://tw.buy.yahoo.com)

after taking time to explore the site, there is a site map (https://tw.buy.yahoo.com/help/helper.asp?p=sitemap&hpp=sitemap) 
that we can use to  get all category (with query pattern /?z= ) and sub category ids (with query pattern /?sub=)

after investigating category and sub category page, there is a section 
called 熱門精選 at right side.  The corresponding html id for this section
is "cl-hotrank".  I will simply assume the item listed in this section will be
the best selling products based on the id name used ('hotrank')

at this point, what we need to do for this crawler would be: 
1. visitng all category and sub category pages 
2. getting all item's url in section with id equals 'cl-hotrank', 
3. collecting item information from each item's url 
4. saving those information in a excel or csv file


Limitation:
1. because there is no way to get the information in terms of actual revenue or 
the quantity the product sold, it relys on the web site to put real HOT ITEMS
here.  
2. although for each individual item page, there is a section called 本分類熱銷榜
(with id = 'cl-ordrank'), I didn't take it for consideration because:
    1. those are items within sub sub category.  If we take sub sub category result
    into consideration in addition to catgoery and sub category, we might get too
    many best selling products.  That might violate the meaning of best selling
    products (if too many best selling products, the what do best selling products
    mean?)

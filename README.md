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
### Example
```
python yb.py --help
Usage: yb.py [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  crawl
  query
  show_category_mapping
```
```
python yb.py show_category_mapping
OrderedDict([('7', ['10', '619', '31', '110', '462', '12', '740', '741', '552', '764', '446', '563', '722', '626', '738', '247', '609', '574', '648', '739', '661', '227']), ('42', ['554', '41', '655', '28
7', '671', '628', '576', '531', '553', '392', '712', '220', '709', '737', '772', '654']), ('32', ['145', '80', '264', '189', '210', '639', '109', '216', '684', '224', '674', '527', '66', '536', '183', '67
5', '769']), ('9', ['35', '461', '687', '686', '19', '100', '679', '744', '749', '756', '511', '371', '267', '730', '678', '222', '482', '546', '397', '560', '670', '672', '433']), ('41', ['42', '4', '592
', '389', '732', '360', '733', '665', '418', '577', '263', '317', '329', '417', '381', '396', '344', '742', '646']), ('47', ['614', '28', '252']), ('3', ['614', '1', '693', '215', '26', '22', '52', '36',
'24', '681', '51', '698', '408', '15', '714', '715', '197', '27', '16']), ('48', ['696', '736', '704', '695']), ('4', ['430', '436', '454', '617', '715', '583', '682', '54', '668', '766', '765']), ('46',
['107', '2', '453', '735']), ('5', ['751', '38', '121', '55', '455', '9', '57', '613', '518', '706', '120', '612', '56', '517', '566']), ('15', ['478', '705', '475', '723', '476', '114', '97', '472', '410
', '11', '605', '757']), ('38', ['277', '463', '18', '459', '591', '206', '484', '282', '259', '525', '535', '443', '449', '309', '203']), ('36', ['673', '83', '692', '466']), ('10', ['676', '23', '104',
'464', '103', '466', '83', '465']), ('43', ['5', '697', '629', '68', '269', '270', '657', '748']), ('8', ['30', '65', '460', '437', '67', '691', '694', '590', '87', '768', '770', '99', '585', '60', '61',
'64', '62', '683', '587', '759', '589', '586']), ('6', ['8', '481', '90', '37', '70', '202', '521', '543', '660', '530', '330', '743', '754']), ('40', ['458', '689', '469', '457']), ('11', ['703', '286',
'468', '470', '85']), ('39', ['710', '7', '34']), ('2', ['43', '72', '14']), ('45', ['718', '720']), ('37', ['409'])])
```
it display available category id and corresponding sub category ids

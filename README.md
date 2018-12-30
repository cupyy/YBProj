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

## Using proxy to avoid blocking
possible solution https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/#5-things-to-keep-in-mind-while-using-proxies-and-rotating-ip-addresses6
implemented the code in lib/webpage.py but currently turn it off because
the operation is not stable

## Handling exception 
https://www.peterbe.com/plog/best-practice-with-retries-with-requests
implemented in lib/webpage.py

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
use --help to get detail explaination
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
```
python yb.py crawl --help
Usage: yb.py crawl [OPTIONS]

Options:
  --cat_id TEXT          Crawl Yahoo Buy with specified category id.  If not
                         specified, it will crawl all category and sub
                         category ids
  --filename TEXT        Specify the filename to save crawled result.  If not
                         specified, name "default" will be used
  --filetype [xlsx|csv]  specify file type to save.  default to xlsx if not
                         specified
  -h, --help             Show this message and exit.
```
To simply crawl all category, just type:
```
python yb.py crawl
```
```
process category 7 hot item
process sub category 10 hot item
process sub category 619 hot item
process sub category 31 hot item
process sub category 110 hot item
process sub category 462 hot item
```
result will be caved to output/default.xlsx

or crawl category id = 45
```
python yb.py crawl --filename cat_45 --cat_id 45
process category 45 hot item
process sub category 718 hot item
process sub category 720 hot item
writting result to output/cat_45.xlsx
```
result will be saved in output/cat_45.xlsx 
```
python yb.py query --help
Usage: yb.py query [OPTIONS]

Options:
  --filename TEXT        Specify the filename for crawled result used for
                         query.  If not specified, name "default" will be used
  --filetype [xlsx|csv]  Specify file type to query from.  Default to xlsx if
                         not specified
  --min_price INTEGER    Minimun price to consider, Default to 0
  --max_price TEXT       Maxmun price to consider, Default to no limit
  --stats_view           Show aggregated result grouped by category instead of
                         raw data.  Default to show product count and average
                         price for each category
  -h, --help             Show this message and exit.
```
query command to perform simple query and aggregation operation
```
python yb.py query --min_price 1000 --max_price 10000
```
will return all raw record with price between 1000 ~ 10000
```
python yb.py query --stats_view
    category_id           category  product_name_count    price_  39   1634.615385
1             3  電腦資訊 / 週邊 / Apple                  98  10546.397959
2             4  手機 / 平板 / 耳機 / 穿戴                  46   7087.521739
3   65  11526.246154
4                    159   2237.352201
6             8     精品 / 手錶 / 珠寶飾品                 125  17905.208000
7             9      女鞋 / 男鞋 / 運動鞋                 179   3424.279330
8            10       收納 / 家具 / 床墊                  43   5251.837209
9            11         健身戶外 / 行李箱                  28   3488.285714
10           15       量販 / 食品 / 醫療                  64    435.015625
11           32                內睡衣                 128   1303.546875
12           36       廚具 / 衛浴 / 寵物                  23   1676.478261
13           37                票券區                  10   3245.600000
14           38       婦幼 / 童裝 / 玩具                  85   1381.517647
15           39         機車 / 汽機車用品                   1   3990.000000
16           40        運動服飾 / 運動用品                  22   1787.590909
17           41       女包 / 男包 / 皮夾                 151   3609.251656
18           42             牛仔休閒服飾                 154   2557.175325
19           43       居家 / 寢具 / 家飾                  55   6841.345455
20           45               禮物專區                   3   2932.666667
21           46     相機 / 攝影機 / 望遠鏡                  15   9341.866667
22           47     電競 / 電玩 / 授權週邊                  27  19991.777778
23           48     智能家居 / 監控 / 辦公                  19   2041.210526
```
will return aggregated result (total product count and average price)  grouped by category


# DM - Product Catalog
DM is a product catalog that apply optimizations of images 
Reduce the image to appropied size and convert it in webp format

## Apps
- opening: show business opening hours.
- publications: posts in social networks.
- products.
- usage_log: stats of searchs performed, viewed products and viewed categories.
- vendors: vendors of products.

## Search Mode

- by product
- by category
- by words


## Category cleaning

The categories that not have products are not shown
If one product is add to one category, then it is showed
It is perform through m2m_change signal and Product.__pre_delete method

## Web convert 

django-webp-converted is used for convert image to webp format


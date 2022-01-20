# DM - Product Catalog


## Apps
- opening: show business opening hours

update_str_schedule: se actualiza cuando hay cambios en una instancia Schedule con relacion a la instacia Opening
o cuando se realizan cambios en la instancia Opening

- publications

String is used in the urls for search the publications 
because if the format of a uuid is broken it does not match urls

- products:
- usage_log:
- vendors

## Search Mode

- by product
- by category
- by words


## Category cleaning

The categories that not have products are not shown
If one product is add to one category, then it is showed
It is perfom through m2m_change signal and Product.__pre_delete method




## Web convert 

Usa django web convert para convertir los estaticos el webp

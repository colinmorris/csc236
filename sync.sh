#!/bin/bash

mkdocs build
cp docs/final/.htaccess site/final
rsync -r site/* colin@cs.toronto.edu:~/public_html/236/W20/

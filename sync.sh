#!/bin/bash

mkdocs build
rsync -r site/* colin@cs.toronto.edu:~/public_html/236/W20/

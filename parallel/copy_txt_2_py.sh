#!/usr/bin/env bash

sudo cat /dev/null > expression1.py
sudo cat /dev/null > expression2.py
sudo cat /dev/null > expression3.py
sudo cat /dev/null > expression4.py
sudo cat /dev/null > expression5.py
sudo cat /dev/null > expression7.py

echo "from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *

eq1 = " > expression1.py

echo "from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *

eq2 = " > expression2.py

echo "from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *

eq3 = " > expression3.py

echo "from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *

eq4 = " > expression4.py

echo "from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *

eq5 = " > expression5.py

echo "from sympy import *
from definitions.generic_coordinates import *
from definitions.constants import *

eq7 = " > expression7.py

cat expand_expression1.txt >> expression1.py
cat expand_expression2.txt >> expression2.py
cat expand_expression3.txt >> expression3.py
cat expand_expression4.txt >> expression4.py
cat expand_expression5.txt >> expression5.py
cat expand_expression7.txt >> expression7.py
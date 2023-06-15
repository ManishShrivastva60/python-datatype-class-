# 1st rule to import module
import package.module1 as manish

manish.add(2, 3)
manish.div(4,3)
manish.mul(4,5)
manish.sub(4,3)
 
# print(module1.a)


# 2nd rule to import

# from package.module1 import sub,div

# sub(3,2)
# div(6,3)

# 3rd rule to import

from package.module1 import *

sub(3,4)
mul(4,5)
div(8,4)
sub(9,4)
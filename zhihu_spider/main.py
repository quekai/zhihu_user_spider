from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# debug结果为403表示知乎检测出了异常流量，要填验证码
execute(["scrapy","crawl","zhihu"])
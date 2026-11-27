# pyafipws still imports configparser.SafeConfigParser, removed in Python 3.12.
import configparser

if not hasattr(configparser, "SafeConfigParser"):
    configparser.SafeConfigParser = configparser.ConfigParser

##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from . import wizard
from . import models

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2


a_device = Device(**srx2)
a_device.open()
a_device.timeout = 60
cfg = Config(a_device)
cfg.lock()
try:
   cfg.lock()
except LockError:
   print("The configuration is already locked !!!")
cfg.load("set system host-name python4life", format="set", merge = True)
print(cfg.diff())
cfg.rollback(0)
print(cfg.diff())
cfg.unlock()


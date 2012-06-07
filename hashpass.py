# -*- coding: utf-8 -*-

"""
Usage:
  >>> ret = hashpass.gen('your password')
  >>> ret
  sha1$Ti238lm+TEmCPgroo2/sqA$/WNnS7UT0uItvD/SqY/O0MCHe+4
  
  >>> hashpass.check('your password', ret)
  True
  
  >>> hashpass.check('bad password', ret)
  False

gen:
  Args:
    password: raw password string.
    algo: hash algorithm. default is sha1.
    stretch: number of stretching. default is 1000.
  
  Returns:
    hashed password string.

check:
  Args:
    password: raw password string.
    target: hashed password string that was returned from gen.
  
  Returns:
    whether if password is correct or not.
"""

import base64
import uuid
import hashlib
import hmac

_ALGO = 'sha1'
_STRETCH = 1000

def gen(password, algo=_ALGO, stretch=_STRETCH):
  salt = _b64encode(uuid.uuid4().bytes)
  ret = _gen(password, salt, algo, stretch)
  return '%s$%s$%s' % (algo, salt, ret)

def check(password, target, stretch=_STRETCH):
  algo, salt, val = target.split('$')
  ret = _gen(password, salt, algo, stretch)
  return ret == val

def _gen(password, salt, algo, stretch):
  password += salt
  mod = getattr(hashlib, algo)
  obj = hmac.new(password, None, mod)
  for _ in xrange(stretch):
    obj.update(password)
  return _b64encode(obj.digest())

def _b64encode(s):
  return base64.standard_b64encode(s).rstrip('=')

def main():
  import sys, time
  s = time.time()
  print gen(sys.argv[1])
  print time.time() - s

if __name__ == '__main__':
  main()

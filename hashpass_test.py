# -*- coding: utf-8 -*-

import uuid
import hashpass

def main():
  
  password = 'test'
  assert hashpass.check(password, 'sha1$0SIN//v0SCuQlnpzvC2TtQ$WkrhcOuwqiOeIYWYE2rook0SzbI')
  assert hashpass.check(password, 'sha1$VD+Idw00RzuJvaHuEhB7Hg$QxUTMBgc+eD3TNVEl4QpTniaTmI')
  assert hashpass.check(password, 'sha1$EUQlWrBpSoecM3gYYpGxow$b8HZ5kGu4hTe2g2pfB4fTJhH2Sg')
  assert hashpass.check(password, 'sha1$h437ZvJFTkWGjS2LDyiIcw$wqCZxwLqCH4dHlk2GUGBbs1s3xM')
  assert hashpass.check(password, 'sha1$cyQluRfxS2WtFjG/fJNEZA$9CTWevy+johvDxhRoyQVMwa5VPA')
  
  password = 'tset'
  assert not hashpass.check(password, 'sha1$0SIN//v0SCuQlnpzvC2TtQ$WkrhcOuwqiOeIYWYE2rook0SzbI')
  assert not hashpass.check(password, 'sha1$VD+Idw00RzuJvaHuEhB7Hg$QxUTMBgc+eD3TNVEl4QpTniaTmI')
  assert not hashpass.check(password, 'sha1$EUQlWrBpSoecM3gYYpGxow$b8HZ5kGu4hTe2g2pfB4fTJhH2Sg')
  assert not hashpass.check(password, 'sha1$h437ZvJFTkWGjS2LDyiIcw$wqCZxwLqCH4dHlk2GUGBbs1s3xM')
  assert not hashpass.check(password, 'sha1$cyQluRfxS2WtFjG/fJNEZA$9CTWevy+johvDxhRoyQVMwa5VPA')
  
  for algo in ('md5', 'sha1', 'sha256'):
    for i in (1, 10, 100, 1000, 10000):
      pwd = uuid.uuid4().hex
      ret = hashpass.gen(pwd, algo, i)
      assert hashpass.check(pwd, ret, i)
      assert not hashpass.check(pwd, ret, i-1)
      assert not hashpass.check(pwd, ret, i+1)
      assert not hashpass.check(pwd+'a', ret, i-1)
      assert not hashpass.check(pwd+'a', ret, i)
      assert not hashpass.check(pwd+'a', ret, i+1)
  
  print 'OK'

if __name__ == '__main__':
  main()

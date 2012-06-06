# -*- coding: utf-8 -*-

import uuid
import hashpass

def main():
  password = 'test'
  assert hashpass.check(password, 'sha1$vGY33ybgTOChctBkyOybkA$t2aX+uybb9s3e2wIcNKmEWhr2xg')
  assert hashpass.check(password, 'sha1$fomfjo8VR6euV4v0cVmHbA$4/wZm9+2U2es8htmSqwMtH+4ofI')
  assert hashpass.check(password, 'sha1$zgBhv/2bQJ6AHjosPW+YHA$KIRF/8E/r7o/EV9p3jLMtQmAXc0')
  assert hashpass.check(password, 'sha1$Kxj+lGtIQfqQmSVtkr+otQ$YgKYpiY+oxrM2UtJQGtgd5Yzm/w')
  assert hashpass.check(password, 'sha1$n9cnSBeCRiKxLVe+sDGjVw$/51mMscfLrPkOA7S/6ZYTviyROo')
  
  password = 'tset'
  assert not hashpass.check(password, 'sha1$vGY33ybgTOChctBkyOybkA$t2aX+uybb9s3e2wIcNKmEWhr2xg')
  assert not hashpass.check(password, 'sha1$fomfjo8VR6euV4v0cVmHbA$4/wZm9+2U2es8htmSqwMtH+4ofI')
  assert not hashpass.check(password, 'sha1$zgBhv/2bQJ6AHjosPW+YHA$KIRF/8E/r7o/EV9p3jLMtQmAXc0')
  assert not hashpass.check(password, 'sha1$Kxj+lGtIQfqQmSVtkr+otQ$YgKYpiY+oxrM2UtJQGtgd5Yzm/w')
  assert not hashpass.check(password, 'sha1$n9cnSBeCRiKxLVe+sDGjVw$/51mMscfLrPkOA7S/6ZYTviyROo')
  
  for algo in ('md5', 'sha1', 'sha256'):
    for i in (1, 10, 100, 1000):
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

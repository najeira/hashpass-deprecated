# -*- coding: utf-8 -*-

import uuid
import hashpass

def main():
  
  password = 'test'
  assert hashpass.check(password, 'sha1$c9dunTK+Rv+JSA/u2Eqn+Q$ozHGjgzOoltVdJ7gQaM4BZaPxHo')
  assert hashpass.check(password, 'sha1$F91SELAoROiDjS3KajfKGA$GQ6IdA+PkfbET7MwfITvB7gCTuE')
  assert hashpass.check(password, 'sha1$MbhKsXkxRoeGCl9pRDwGnA$B/4NtNiJ3GAW/zP6/0tiM5Mdbfo')
  assert hashpass.check(password, 'sha1$N9tbpINlTS+GcV3Vt9JR/Q$z7AsnUL7t0BiNJDlfDdfjYvE06U')
  assert hashpass.check(password, 'sha1$Vq4bkWK+Q5uXFKh8zlTMNQ$0+FZgfMOR8ckY/+cI8ZvWYLg0xQ')
  
  password = 'tset'
  assert not hashpass.check(password, 'sha1$c9dunTK+Rv+JSA/u2Eqn+Q$ozHGjgzOoltVdJ7gQaM4BZaPxHo')
  assert not hashpass.check(password, 'sha1$F91SELAoROiDjS3KajfKGA$GQ6IdA+PkfbET7MwfITvB7gCTuE')
  assert not hashpass.check(password, 'sha1$MbhKsXkxRoeGCl9pRDwGnA$B/4NtNiJ3GAW/zP6/0tiM5Mdbfo')
  assert not hashpass.check(password, 'sha1$N9tbpINlTS+GcV3Vt9JR/Q$z7AsnUL7t0BiNJDlfDdfjYvE06U')
  assert not hashpass.check(password, 'sha1$Vq4bkWK+Q5uXFKh8zlTMNQ$0+FZgfMOR8ckY/+cI8ZvWYLg0xQ')
  
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

<?php

require_once('hashpass.php');
$password = 'test';
assert(hashpass_check($password, 'sha1$c9dunTK+Rv+JSA/u2Eqn+Q$ozHGjgzOoltVdJ7gQaM4BZaPxHo'));
assert(hashpass_check($password, 'sha1$F91SELAoROiDjS3KajfKGA$GQ6IdA+PkfbET7MwfITvB7gCTuE'));
assert(hashpass_check($password, 'sha1$MbhKsXkxRoeGCl9pRDwGnA$B/4NtNiJ3GAW/zP6/0tiM5Mdbfo'));
assert(hashpass_check($password, 'sha1$N9tbpINlTS+GcV3Vt9JR/Q$z7AsnUL7t0BiNJDlfDdfjYvE06U'));
assert(hashpass_check($password, 'sha1$Vq4bkWK+Q5uXFKh8zlTMNQ$0+FZgfMOR8ckY/+cI8ZvWYLg0xQ'));
$password = 'tset';
assert(!hashpass_check($password, 'sha1$c9dunTK+Rv+JSA/u2Eqn+Q$ozHGjgzOoltVdJ7gQaM4BZaPxHo'));
assert(!hashpass_check($password, 'sha1$F91SELAoROiDjS3KajfKGA$GQ6IdA+PkfbET7MwfITvB7gCTuE'));
assert(!hashpass_check($password, 'sha1$MbhKsXkxRoeGCl9pRDwGnA$B/4NtNiJ3GAW/zP6/0tiM5Mdbfo'));
assert(!hashpass_check($password, 'sha1$N9tbpINlTS+GcV3Vt9JR/Q$z7AsnUL7t0BiNJDlfDdfjYvE06U'));
assert(!hashpass_check($password, 'sha1$Vq4bkWK+Q5uXFKh8zlTMNQ$0+FZgfMOR8ckY/+cI8ZvWYLg0xQ'));

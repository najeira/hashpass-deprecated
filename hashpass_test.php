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

foreach (array('md5', 'sha1', 'sha256') as $algo) {
	foreach (array(1, 10, 100, 1000, 10000) as $i) {
		$pwd = uniqid('', true);
		$ret = hashpass_gen($pwd, $algo, $i);
		assert(hashpass_check($pwd, $ret, $i));
		assert(!hashpass_check($pwd, $ret, $i-1));
		assert(!hashpass_check($pwd, $ret, $i+1));
		assert(!hashpass_check($pwd+'a', $ret, $i-1));
		assert(!hashpass_check($pwd+'a', $ret, $i));
		assert(!hashpass_check($pwd+'a', $ret, $i+1));
	}
}

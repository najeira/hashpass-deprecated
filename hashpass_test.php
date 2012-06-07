<?php

require_once('hashpass.php');

$password = 'test';
assert(hashpass_check($password, 'sha1$0SIN//v0SCuQlnpzvC2TtQ$WkrhcOuwqiOeIYWYE2rook0SzbI'));
assert(hashpass_check($password, 'sha1$VD+Idw00RzuJvaHuEhB7Hg$QxUTMBgc+eD3TNVEl4QpTniaTmI'));
assert(hashpass_check($password, 'sha1$EUQlWrBpSoecM3gYYpGxow$b8HZ5kGu4hTe2g2pfB4fTJhH2Sg'));
assert(hashpass_check($password, 'sha1$h437ZvJFTkWGjS2LDyiIcw$wqCZxwLqCH4dHlk2GUGBbs1s3xM'));
assert(hashpass_check($password, 'sha1$cyQluRfxS2WtFjG/fJNEZA$9CTWevy+johvDxhRoyQVMwa5VPA'));

$password = 'tset';
assert(!hashpass_check($password, 'sha1$0SIN//v0SCuQlnpzvC2TtQ$WkrhcOuwqiOeIYWYE2rook0SzbI'));
assert(!hashpass_check($password, 'sha1$VD+Idw00RzuJvaHuEhB7Hg$QxUTMBgc+eD3TNVEl4QpTniaTmI'));
assert(!hashpass_check($password, 'sha1$EUQlWrBpSoecM3gYYpGxow$b8HZ5kGu4hTe2g2pfB4fTJhH2Sg'));
assert(!hashpass_check($password, 'sha1$h437ZvJFTkWGjS2LDyiIcw$wqCZxwLqCH4dHlk2GUGBbs1s3xM'));
assert(!hashpass_check($password, 'sha1$cyQluRfxS2WtFjG/fJNEZA$9CTWevy+johvDxhRoyQVMwa5VPA'));

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

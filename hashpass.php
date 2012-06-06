<?php

function hashpass_gen($password, $algo='sha1', $stretch=1000) {
	$salt = rtrim(base64_encode(uniqid()), '=');
	$ret = _hashpass_gen($password, $salt, $algo, $stretch);
	return sprintf('%s$%s$%s', $algo, $salt, $ret);
}

function _hashpass_gen($password, $salt, $algo, $stretch) {
	$res = hash_init($algo, HASH_HMAC, $password);
	for ($i = 0; $i < $stretch; $i++) {
		hash_update($res, $salt);
	}
	$ret = hash_final($res, true);
	return rtrim(base64_encode($ret), '=');
}

function hashpass_check($password, $target, $stretch=1000) {
	list($algo, $salt, $val) = explode('$', $target);
	$ret = _hashpass_gen($password, $salt, $algo, $stretch);
	return $ret === $val;
}

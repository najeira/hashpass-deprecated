hashpass
========

A library to hash password with salt and streching.

A function `gen` returns hashed string that include
name of hash algorithm, salt and hashed password.

It will be like this:

    sha1$Ti238lm+TEmCPgroo2/sqA$/WNnS7UT0uItvD/SqY/O0MCHe+4

A function `check` returns whether password is correct or not.


Usage
-----

### Python

    import hashpass
    
    # gen returns hashed string,
    hashed = hashpass.gen('your password')
    
    # check returns whether password is correct or not.
    ret = hashpass.check('your password', hashed)
    # ret is True
    
    ret = hashpass.check('bad password', hashed)
    # ret is False


### PHP

    require_once('hashpass.php');
    
    $hashed = hashpass_gen('your password');
    
    $ret = hashpass_check('your password', $hashed);


License
-------

* Copyright: 2012 by najeira.
* License: MIT

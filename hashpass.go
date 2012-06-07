package hashpass

import (
	"fmt"
	"hash"
	"bytes"
	"time"
	"strings"
	"math/rand"
	"encoding/base64"
	"encoding/binary"
	"crypto/hmac"
	"crypto/md5"
	"crypto/sha1"
	"crypto/sha256"
	"crypto/sha512"
)

var hashNameMap = map[string]func() hash.Hash {
	"md5": md5.New,
	"sha1": sha1.New,
	"sha224": sha256.New224,
	"sha256": sha256.New,
	"sha384": sha512.New384,
	"sha512": sha512.New,
}

var rander = rand.New(rand.NewSource(time.Now().Unix()))

func Gen(password string, algo string, stretch int) string {
	salt := _salt()
	ret := _gen(password, salt, algo, stretch)
	return fmt.Sprintf("%s$%s$%s", algo, salt, ret)
}

func Check(password string, target string, stretch int) bool {
	arr := strings.Split(target, "$")
	algo, salt, val := arr[0], arr[1], arr[2]
	ret := _gen(password, salt, algo, stretch)
	return val == ret
}

func _gen(password, salt string, algo string, stretch int) string {
	pwd := []byte(password + salt)
	f := hashNameMap[algo]
	res := hmac.New(f, pwd)
	for i := 0; i < stretch; i++ {
		res.Write(pwd)
	}
	return _encode(res.Sum(nil))
}

func _salt() string {
	buf := new(bytes.Buffer)
	for buf.Len() < 16 {
		binary.Write(buf, binary.LittleEndian, rander.Int31())
	}
	return _encode(buf.Bytes())
}

func _encode(s []byte) string {
	rets := base64.StdEncoding.EncodeToString(s)
	return strings.TrimRight(rets, "=")
}

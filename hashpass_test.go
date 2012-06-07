package hashpass

import (
	//"fmt"
	"testing"
)

func TestHASHPASS(t *testing.T) {
	stretch := 1000
	rets := []string{
		"sha1$0SIN//v0SCuQlnpzvC2TtQ$WkrhcOuwqiOeIYWYE2rook0SzbI",
		"sha1$VD+Idw00RzuJvaHuEhB7Hg$QxUTMBgc+eD3TNVEl4QpTniaTmI",
		"sha1$EUQlWrBpSoecM3gYYpGxow$b8HZ5kGu4hTe2g2pfB4fTJhH2Sg",
		"sha1$h437ZvJFTkWGjS2LDyiIcw$wqCZxwLqCH4dHlk2GUGBbs1s3xM",
		"sha1$cyQluRfxS2WtFjG/fJNEZA$9CTWevy+johvDxhRoyQVMwa5VPA",
	}
	
	pwd := "test"
	for _, ret := range rets {
		if !Check(pwd, ret, stretch) {
			t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd, ret, stretch)
		}
	}
	
	pwd = "tset"
	for _, ret := range rets {
		if Check(pwd, ret, stretch) {
			t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd, ret, stretch)
		}
	}
	
	algos := []string{"md5", "sha1", "sha256"}
	stretches := []int{1, 10, 100, 1000, 10000}
	for _, algo := range algos {
		var ret string
		for _, stretch := range stretches {
			ret = Gen(pwd, algo, stretch)
			
			chk := pwd
			if !Check(chk, ret, stretch) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch)
			}
			if Check(chk, ret, stretch - 1) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch - 1)
			}
			if Check(chk, ret, stretch + 1) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch + 1)
			}
			if ret == Gen(chk, algo, stretch) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch)
			}
			
			chk = pwd + "a"
			if Check(chk, ret, stretch - 1) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch - 1)
			}
			if Check(chk, ret, stretch) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch)
			}
			if Check(chk, ret, stretch + 1) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch + 1)
			}
			if ret == Gen(chk, algo, stretch) {
				t.Errorf("chk=%s, ret=%s, stretch=%s\n", chk, ret, stretch)
			}
		}
		//fmt.Println(ret)
	}
}

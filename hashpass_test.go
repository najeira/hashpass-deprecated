package hashpass

import (
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
		for _, stretch := range stretches {
			ret := Gen(pwd, algo, stretch)
			if !Check(pwd, ret, stretch) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd, ret, stretch)
			}
			if Check(pwd, ret, stretch - 1) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd, ret, stretch - 1)
			}
			if Check(pwd, ret, stretch + 1) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd, ret, stretch + 1)
			}
			if Check(pwd+"a", ret, stretch - 1) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd + "a", ret, stretch - 1)
			}
			if Check(pwd+"a", ret, stretch) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd + "a", ret, stretch)
			}
			if Check(pwd+"a", ret, stretch + 1) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd + "a", ret, stretch + 1)
			}
			if ret == Gen(pwd+"a", algo, stretch) {
				t.Errorf("pwd=%s, ret=%s, stretch=%s\n", pwd + "a", ret, stretch)
			}
		}
	}
}

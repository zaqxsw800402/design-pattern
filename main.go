package main

import "fmt"

type p struct {
	name string
}

func main() {
	res := make([]p, 0)
	check2 := make([]p, 0)
	check := make([]*p, 0)
	res = append(res, p{name: "a"}, p{name: "b"})

	for _, v := range res {
		if v.name == "a" {
			v.name = "d"
		} else {
			v.name = "c"
		}
		fmt.Println(v)
		check = append(check, &v)
		check2 = append(check2, v)
	}

	for _, v := range check {

		fmt.Println(*v)
	}
	fmt.Println(check2)
}

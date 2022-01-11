package main

import "fmt"

type human interface {
	Age() int
}

type person struct {
	age int
}

func (p person) Age() int {
	return p.age
}

type tw struct {
	person
}

func (t tw) String() string {
	return fmt.Sprintf("ags: %v", t.age)
}

func main() {
	a := tw{person{age: 39}}
	a.age = 20
	i := a.Age()
	fmt.Println(i)
	fmt.Println(a.String())
}

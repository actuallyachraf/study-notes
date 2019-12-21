package main

import "fmt"

type State int

// Possible States
const (
	Start State = iota
	Halt
	MoveRight
	MoveLeft
	Compare
)

// Turing Machine
type TuringMachine struct {
	InputTape  []byte
	InputHead  int
	WorkTape   []byte
	WorkHead   int
	OutputTape []byte
	OutputHead int
	Register   State
}

func (m *TuringMachine) Read(tape string) byte {
	switch tape {
	case "input":
		return m.InputTape[m.InputHead]
	case "work":
		return m.WorkTape[m.WorkHead]
	}
	return m.OutputTape[m.OutputHead]
}

func (m *TuringMachine) Write(val byte, tape string) {
	switch tape {
	case "input":
		m.InputTape[m.InputHead] = val
	case "work":
		m.WorkTape[m.WorkHead] = val
	case "output":
		m.OutputTape[m.OutputHead] = val
	}
}

// Alphabet
var (
	ONE   = byte(1)
	ZERO  = byte(0)
	BLANK = byte(2)
)

func PAL(m *TuringMachine, input []byte) {

	copy(m.InputTape, input)
	copy(m.WorkTape, input)

	m.InputHead = 0
	m.WorkHead = len(input) - 1

	m.Register = Start
	for m.Register != Halt && m.WorkHead > 0 {

		inputCell := m.Read("input")
		workCell := m.Read("work")

		if workCell != inputCell {
			m.Write(ONE, "output")
			m.Register = Halt
		} else {
			m.InputHead++
			m.WorkHead--
		}
	}
}
func main() {
	var M = TuringMachine{
		InputTape:  make([]byte, 8),
		WorkTape:   make([]byte, 8),
		OutputTape: make([]byte, 1),
		Register:   Start,
	}
	input := []byte{0, 1, 1, 1, 0}
	input1 := []byte{0, 1, 1, 1}
	PAL(&M, input)

	fmt.Println(M.Read(""))

	PAL(&M, input1)
	fmt.Println(M.Read(""))
}

import pytest
from src.custom_stack_class import *

def test_push_one_elementinstack():
    element_value = 5.0
    value = 0.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

def test_fullstack():
    cut = CustomStack(1)
    cut.push('elefante')
    with pytest.raises(StackFullException):
        cut.push('elefante2')

def test_popreturnlastelement():
    cut = CustomStack(1)
    cut.push("elefante")
    assert cut.pop() == "elefante"
    with pytest.raises(StackEmptyException):
        cut.pop()

def test_top():
    cut = CustomStack(1)
    with pytest.raises(StackEmptyException):
        cut.top()
    
def test_sort_with_six_elements():
    stack = CustomStack(6)
    numeros = [45, 3, 12, 30, 7, 25]
    for n in numeros:
        stack.push(n)
    
    sorteio = NumberAscOrder()
    result = sorteio.sort(stack)
    assert result == sorted(numeros)

def test_sort_with_empty_stack():
    stack = CustomStack(6)
    sorteio = NumberAscOrder()
    result = sorteio.sort(stack)
    assert result == []
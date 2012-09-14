import theano
from theano.gof.utils import give_variables_names, unique

def test_give_variables_names():
    x = theano.tensor.matrix('x')
    y = x + 1
    z = theano.tensor.dot(x, y)
    variables = (x, y, z)
    give_variables_names(variables)
    assert all(var.name for var in variables)
    assert unique([var.name for var in variables])

def test_give_variables_names_small():
    x = theano.tensor.matrix('x')
    y = theano.tensor.dot(x, x)
    fgraph = theano.FunctionGraph((x,), (y,))
    give_variables_names(fgraph.variables)
    assert all(var.name for var in fgraph.variables)
    assert unique([var.name for var in fgraph.variables])


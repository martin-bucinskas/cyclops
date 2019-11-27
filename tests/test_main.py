import pytest

from cyclops.data.Function import Function
from cyclops.main import function_list_to_map


def test_function_list_to_map():
    f1 = Function({'FunctionName': 'test-1'})
    f2 = Function({'FunctionName': 'test-2'})
    function_list = [f1, f2]

    expected_function_map = {
        'test-1': f1,
        'test-2': f2
    }

    function_map = function_list_to_map(function_list)

    assert function_map == expected_function_map

import pytest
from unittest.mock import patch

from cyclops.data.Function import Function
from cyclops.cyclops import function_list_to_map, get_all_lambdas


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


def test_get_all_lambdas_status_ok():
    f1 = {
        'ResponseMetadata': {
            'HTTPStatusCode': 200
        },
        'Functions': [
            {'FunctionName': 'test-0'},
            {'FunctionName': 'test-1'}
        ]
    }

    function_list = get_all_lambdas(f1)

    count = 0
    for function in function_list:
        assert function.FunctionName == 'test-' + str(count)
        count += 1


def test_get_all_lambdas_status_internal_server_error():
    f1 = {
        'ResponseMetadata': {
            'HTTPStatusCode': 500
        },
        'Functions': [
            {'FunctionName': 'test-0'},
            {'FunctionName': 'test-1'}
        ]
    }

    function_list = get_all_lambdas(f1)

    assert len(function_list) == 0


def test_main():
    assert 1 == 1

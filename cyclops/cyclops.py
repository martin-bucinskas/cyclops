import logging
import boto3
from botocore.exceptions import ClientError
import pprint

from cyclops.cli.function_display import CLIFunctionDisplay
from cyclops.cli.function_select import CLIFunctionSelect
from cyclops.data.Function import Function

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def get_all_lambdas(response_list_functions):
    response_metadata = response_list_functions['ResponseMetadata']
    functions = response_list_functions['Functions']
    function_list = []

    if response_metadata['HTTPStatusCode'] == 200:
        for function in functions:
            obj_function = Function(function)
            function_list.append(obj_function)

    return function_list


def function_list_to_map(function_list):
    function_map = {}
    for function in function_list:
        function_map[function.FunctionName] = function
    return function_map


def get_lambda_client(aws_profile_name, region_name='eu-west-1'):
    session = boto3.Session(profile_name=aws_profile_name, region_name=region_name)
    lambda_client = session.client('lambda')

    return lambda_client


def main(aws_profile_name):
    lambda_client = get_lambda_client(aws_profile_name)
    response_list_functions = lambda_client.list_functions()

    function_list = get_all_lambdas(response_list_functions)
    function_map = function_list_to_map(function_list)

    while True:
        cli_function_select = CLIFunctionSelect(function_list)
        user_selected_lambda = cli_function_select.display()
        obj_function = function_map.get(user_selected_lambda)

        if user_selected_lambda == 'Quit':
            break

        cli_function_display = CLIFunctionDisplay(obj_function)
        user_selected_operation = cli_function_display.display()

        if user_selected_operation == 'Quit':
            break

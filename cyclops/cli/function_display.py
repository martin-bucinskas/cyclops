from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
from clint.textui import puts, colored, indent


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',
    Token.Answer: '#f44336 bold',
    Token.Question: ''
})

ui = {
    'type': 'list',
    'message': 'Lambda Operations',
    'name': 'operation',
    'validate': lambda answer: 'You must choose an operation.' if len(answer) == 0 else True,
    'choices': [
        {'name': '<- Back'},
        {'name': 'Invoke'},
        {'name': 'Show Environment Variables'},
        {'name': 'Add Permission'},
        {'name': 'Remove Permission'},
        {'name': 'Create Alias'},
        {'name': 'Delete Alias'},
        {'name': 'Delete Function'},
        {'name': 'Publish Version'},
        {'name': 'Put Function Concurrency'},
        {'name': 'Remove Layer Version Permission'},
        {'name': '<- Quit'}
    ]
}


class CLIFunctionDisplay:

    def __init__(self, obj_function):
        self.obj_function = obj_function

    def display(self):

        with indent(4, quote='|'):
            puts(colored.red('Function Name:\t') + self.obj_function.FunctionName)
            puts(colored.red('ARN:\t\t') + self.obj_function.FunctionArn)
            puts(colored.red('Role:\t\t') + self.obj_function.Role)
            puts(colored.blue('Runtime:\t\t') + self.obj_function.Runtime)
            puts(colored.blue('Handler:\t\t') + self.obj_function.Handler)
            puts(colored.red('Last Modified:\t') + self.obj_function.LastModified)
        print()

        selected_function = prompt(ui, style=style)
        return selected_function['operation']
        pass

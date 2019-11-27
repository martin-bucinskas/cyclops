from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',
    Token.Answer: '#f44336 bold',
    Token.Question: ''
})


class CLIFunctionSelect:

    def __init__(self, function_list):
        self.function_list = function_list

    def create_display(self):
        ui = {
            'type': 'list',
            'message': 'Select Lambda for more details',
            'name': 'selected_lambda',
            'validate': lambda answer: 'You must choose a lambda function.' if len(answer) == 0 else True,
        }

        choices = []

        for function in self.function_list:
            choice = {
                'name': function.FunctionName
            }
            choices.append(choice)

        choices.append({'name': 'Quit'})
        ui['choices'] = choices

        return ui

    def display(self):
        questions = self.create_display()
        selected_function = prompt(questions, style=style)
        return selected_function['selected_lambda']

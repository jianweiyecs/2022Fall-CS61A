test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '28893e4c2667b89b674188e063237622',
          'choices': [
            'A lambda expression does not automatically bind the function that it returns to a name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following statements describes a difference between a def statement and a lambda expression?'
        },
        {
          'answer': '2ad3e8f40fd1b51f9a33075a0048a5d6',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many formal parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'caa97dd5ae148cd72efcf98ef6f4b913',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> lambda x: x  # A lambda expression with one parameter x
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          d330e4294a4387ed4475ee0e95da5386
          # locked
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          0f10194daf41a11a30f4adc80d959f28
          # locked
          >>> b = lambda x, y: lambda: x + y # Lambdas can return other lambdas!
          >>> c = b(8, 4)
          >>> c
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> c()
          bb673dbcb74b8a503ccca3a123f8ac69
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          9024755e0e6b1907cc6e80a977eb6fa3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          ab06d135c02ab203238caafbf77976ce
          # locked
          >>> higher_order_lambda(g)(2)
          ef6b0e7c554b5515158e88d1ee908645
          # locked
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          0f10194daf41a11a30f4adc80d959f28
          # locked
          >>> print_lambda = lambda z: print(z) # When is the return expression of a lambda expression executed?
          >>> print_lambda
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> one_thousand = print_lambda(1000)
          406c98af0b3aa9a2c9dbd76d898bcda3
          # locked
          >>> one_thousand # What did the call to print_lambda return? If it displays nothing, write Nothing
          358b0ae001277273d8cd480ce5dbfb82
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}

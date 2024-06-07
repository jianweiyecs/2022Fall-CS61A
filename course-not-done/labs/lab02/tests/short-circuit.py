test = {
  'name': 'The Truth Will Prevail',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          7edad8d629f285ca759c95da679fd452
          # locked
          >>> False or 0
          b33f256984c474b4181f5512601c4a70
          # locked
          >>> not 10
          30612a20c5efd351c827ed74fa104597
          # locked
          >>> not None
          2363e0cf1475978bc3373849c76acf77
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> True and 1 / 0  # If this errors, just type Error.
          ab06d135c02ab203238caafbf77976ce
          # locked
          >>> True or 1 / 0  # If this errors, just type Error.
          2363e0cf1475978bc3373849c76acf77
          # locked
          >>> -1 and 1 > 0 # If this errors, just type Error.
          2363e0cf1475978bc3373849c76acf77
          # locked
          >>> -1 or 5
          6b4205ba72f3ab35b0da9ecb25ba19dc
          # locked
          >>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
          cf2e1ad2c681425ba709dfa2ee9bde0f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> print(3) or ""
          0f10194daf41a11a30f4adc80d959f28
          c8d065903354f375f887443cb1120aca
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     if x == 0:
          ...         return "zero"
          ...     elif x > 0:
          ...         return "positive"
          ...     else:
          ...         return ""
          >>> 0 or f(1)
          828dc7251d7bf60d6c72dc1d43e8a98f
          # locked
          >>> f(0) or f(-1)
          529cfd7a836a98e3819be429f4f84894
          # locked
          >>> f(0) and f(-1)
          c8d065903354f375f887443cb1120aca
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

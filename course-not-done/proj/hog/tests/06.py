test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> always_roll(3)(10, 20)
          16e2cf37e8254529473d9e0a36b75fcb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> always_roll(0)(99, 99)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

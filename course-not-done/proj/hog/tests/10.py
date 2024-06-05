test = {
  'name': 'Question 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tail_strategy(40, 51, threshold=7, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_strategy(40, 53, threshold=7, num_rolls=2)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_strategy(40, 51, threshold=12, num_rolls=5)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_strategy(40, 52, threshold=7, num_rolls=2)
          962aea5f59fc55bd65ccacf4603c8f22
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> s = 0
          >>> while s < 100:
          ...     if tail_points(s) >= 10:
          ...         assert tail_strategy(90, s, threshold=10, num_rolls=3) == 0
          ...     else:
          ...         assert tail_strategy(90, s, threshold=10, num_rolls=3) == 3
          ...     s += 1
          """,
          'hidden': False,
          'locked': False,
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

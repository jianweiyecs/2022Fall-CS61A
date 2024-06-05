test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> tail_points(25)
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(52)
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(0)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(7)
          af0b3285304485122429774c0ea3182a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(22)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(122)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(584)
          872dbe4a4fe5d8451aa842c21194c866
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = tail_points(23)
          >>> a # check that the value is being returned, not printed
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tail_points(12345)
          3
          >>> # ban str and indexing (lists)
          >>> test.check('hog.py', 'tail_points', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

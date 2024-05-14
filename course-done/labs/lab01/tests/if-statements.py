test = {
  'name': 'What If?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def ab(c, d):
          ...     if c > 5:
          ...         print(c)
          ...     elif c > 7:
          ...         print(d)
          ...     print('foo')
          >>> ab(10, 20)
          32606b4d8bc69544a1579aca287813dc
          076de7ac11ca62f75f649af9dbe4149a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def bake(cake, make):
          ...    if cake == 0:
          ...        cake = cake + 1
          ...        print(cake)
          ...    if cake == 1:
          ...        print(make)
          ...    else:
          ...        return cake
          ...    return make
          >>> bake(0, 29)
          f26f9ec9ba426ebfdd8a43b22c8c74a0
          886cfa066159edb2578269b4d55d2239
          886cfa066159edb2578269b4d55d2239
          # locked
          >>> bake(1, "mashed potatoes")
          18079ca0c56c783746b70728120f3747
          575e1338b070e905f49b16443a77012f
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

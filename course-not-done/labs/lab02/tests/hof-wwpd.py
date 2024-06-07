test = {
  'name': 'Higher Order Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          0127137631d037670fa6a894e2d548ee
          # locked
          >>> chocolate
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> chocolate()
          28f5a700252060ec3bbc4bf4ca744c56
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          28f5a700252060ec3bbc4bf4ca744c56
          # locked
          >>> more_chocolate
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> # Reminder: cake, more_cake, and chocolate were defined/assigned in the code above! 
          >>> # It might be helpful to refer to their definitions on the assignment website so you don't have to scroll as much!
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return chocolate
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          4f02258d689b15b516174b381ad2aef8
          # locked
          >>> snake(10, 20)()
          28f5a700252060ec3bbc4bf4ca744c56
          7fccab88a7c3c0cbffe0142e723d1984
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          c06666e98ec36af7add28e636f1488ee
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

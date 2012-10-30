import re


def find(pattern, text):
    """
    .  - (dot) any char
    \w - word char
    \d - digit
    \s - whitespace
    \S - non-whitespace
    +  - 1 or more
    *  - 0 or more
    """
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return 'not found'


def test_find():

    assert find('igs', 'called piiig') == 'not found'
    assert find('ig', 'called piiig') == 'ig'
    assert find('...g', 'called piiig') == 'iiig'
    assert find('x...g', 'called piiig') == 'not found'
    assert find('..gs', 'called piiig') == 'not found'
    assert find('..g', 'called piiig   much better: xyzg') == 'iig'
    assert find('x..g', 'called piiig   much better: xyzg') == 'xyzg'
    assert find(r'c\.l', 'c.lled piiig   much better: xyzgs') == 'c.l'
    assert find(r':\w\w\w', 'blah :cat blah blah') == ':cat'
    assert find(r'\d\d\d', 'blah :123xxx') == '123'
    assert find(r'\d\s\d\s\d', '1 2 3') == '1 2 3'
    assert find(r'\d\s+\d\s+\d', '1     2  3') == '1     2  3'
    assert find(r':\w+', 'blah :cat blah blah') == ':cat'
    assert find(r':\w+', 'blah :cat123 blah blah') == ':cat123'
    assert find(r':\w+', 'blah :cat123& blah blah') == ':cat123'
    assert find(r':\S+', 'blah :cat123&a=123&dladladla blah blah')\
     == ':cat123&a=123&dladladla'
    assert find(r'\w+@\w+', 'blah khimichenko.vladislav@gmail.com yatta @')\
    == 'vladislav@gmail'
    assert find(r'[\w.]+@[\w.]+', 'blah khimichenko.vladislav@gmail.com yatta @')\
    == 'khimichenko.vladislav@gmail.com'
    assert find(r'[\w.]+@[\w.]+', 'blah khimichenko .vladislav@gmail.com yatta @')\
    == '.vladislav@gmail.com'
    assert find(r'\w[\w.]*@[\w.]+', 'blah khimichenko .vladislav@gmail.com yatta @')\
    == 'vladislav@gmail.com'

    m = re.search(r'(\w[\w.]*)@([\w.]+)','blah khimichenko.vladislav@gmail.com yatta @')
    assert m.group() == 'khimichenko.vladislav@gmail.com'
    assert m.group(1) == 'khimichenko.vladislav'
    assert m.group(2) == 'gmail.com'

    assert re.findall(r'\w[\w.]*@[\w.]+','blah khimichenko.vladislav@gmail.com foo@bar')\
    == ['khimichenko.vladislav@gmail.com', 'foo@bar']
    assert re.findall(r'(\w[\w.]*)@([\w.]+)','blah khimichenko.vladislav@gmail.com foo@bar')\
    == [('khimichenko.vladislav', 'gmail.com'), ('foo','bar')]

    print 'Test find passed ok!'


def main():
    test_find()


if __name__ == "__main__":
    exit(main())

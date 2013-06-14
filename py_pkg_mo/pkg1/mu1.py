from pkg2.mu2 import mod_two

class mod_one(object):
    def f1(self):
        print('this is mod_one - f1')

        print('in mod_one-f1 > invoke mod_two-f2')
        m_2 = mod_two()
        m_2.f2()
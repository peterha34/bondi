import abb

R = abb.Robot(ip='192.168.125.1')
R.buffer_add([[403.82,14.15,346.27], [0,0,3,0]])
R.buffer_execute()

import hubo_ach as ha
import math
import ach
import sys
import time
import datetime
from ctypes import *
	
# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()

[statuss, framesizes] = s.get(state, wait=False, last=False)

ref.ref[ha.RKN] = 0.5
ref.ref[ha.LKN] = 0.5
ref.ref[ha.RHP] = -0.25
ref.ref[ha.LHP] = -0.25
ref.ref[ha.RAP] = -0.25
ref.ref[ha.LAP] = -0.25

r.put(ref)
time.sleep(4)

ref.ref[ha.LHR] = -0.04
ref.ref[ha.RHR] = -0.04
ref.ref[ha.RAR] = 0.04
ref.ref[ha.LAR] = 0.04
r.put(ref)
time.sleep(4);

ref.ref[ha.LHR] = -0.09
ref.ref[ha.RHR] = -0.09
ref.ref[ha.RAR] = 0.09
ref.ref[ha.LAR] = 0.09
r.put(ref)
time.sleep(4);

ref.ref[ha.LHR] = -0.11
ref.ref[ha.RHR] = -0.11
ref.ref[ha.RAR] = 0.11
ref.ref[ha.LAR] = 0.11
r.put(ref)
time.sleep(3);

ref.ref[ha.RKN] = 0.6
ref.ref[ha.RHP] = -0.47
ref.ref[ha.RAP]=0
r.put(ref)
time.sleep(3)
ref.ref[ha.LKN] = 0.65
ref.ref[ha.LAP] = -0.4
r.put(ref)

ref.ref[ha.RKN] = 0.7
ref.ref[ha.RHP] = -0.7
ref.ref[ha.RAP]=-0.02
ref.ref[ha.LKN] = 0.8
ref.ref[ha.LAP] = -0.5
r.put(ref)
time.sleep(2)

ref.ref[ha.LKN] = 0.5

r.put(ref)
time.sleep(2)

ref.ref[ha.LHR] = -0.09
ref.ref[ha.RHR] = -0.09
ref.ref[ha.RAR] = 0.09
ref.ref[ha.LAR] = 0.09
r.put(ref)
time.sleep(2);

ref.ref[ha.LKN] = 0.6
ref.ref[ha.LHP] = -0.57
ref.ref[ha.LAP]=0
ref.ref[ha.RKN] = 0.7
ref.ref[ha.RAP] = -0.5
r.put(ref)
time.sleep(3)

ref.ref[ha.RKN] = 0.6
ref.ref[ha.RHP] = -0.47
ref.ref[ha.RAP]=0
ref.ref[ha.LKN] = 0.65
ref.ref[ha.LAP] = -0.4
r.put(ref)
time.sleep(1)
ref.ref[ha.LKN] = 0.7
ref.ref[ha.LHP] = -0.7
ref.ref[ha.LAP]=-0.02
ref.ref[ha.RKN] = 0.8
ref.ref[ha.RAP] = -0.6
r.put(ref)
time.sleep(1)
ref.ref[ha.LHR] = -0.04
ref.ref[ha.RHR] = -0.04
ref.ref[ha.RAR] = 0.04
ref.ref[ha.LAR] = 0.04
r.put(ref)
time.sleep(2);
ref.ref[ha.RKN] = 0.5
ref.ref[ha.LKN] = 0.5
ref.ref[ha.RHP] = -0.25
ref.ref[ha.LHP] = -0.25
ref.ref[ha.RAP] = -0.25
ref.ref[ha.LAP] = -0.25
time.sleep(2)



ref.ref[ha.LHR] = 0.04
ref.ref[ha.RHR] = 0.04
ref.ref[ha.RAR] = -0.04
ref.ref[ha.LAR] = -0.04
r.put(ref)
time.sleep(2);

#
ref.ref[ha.LHR] = 0.09
ref.ref[ha.RHR] = 0.09
ref.ref[ha.RAR] = -0.09
ref.ref[ha.LAR] = -0.09
r.put(ref)
time.sleep(2);





ref.ref[ha.LHR] = -0.04
ref.ref[ha.RHR] = -0.04
ref.ref[ha.RAR] = 0.04
ref.ref[ha.LAR] = 0.04
r.put(ref)



ref.ref[ha.LHR] = -0.09
ref.ref[ha.RHR] = -0.09
ref.ref[ha.RAR] = 0.09
ref.ref[ha.LAR] = 0.09
ref.ref[ha.RKN] = 0.5
r.put(ref)

time.sleep(1)





























# Close the connection to the channels
r.close()
s.close()

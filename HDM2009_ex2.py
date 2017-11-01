#############
#This is neuron with python example from 
#the third figure from the paper
#NEURON and Python
#Michael L. Hines  , Andrew P. Davison and Eilif Muller
#Frontiers in neuroinformatics, 2009
#
###########


from neuron import h,gui

# create pre - and post - synaptic sections
pre = h.Section ()
post = h.Section ()
for sec in pre , post :
	sec.insert('hh')

# inject current in the pre - synaptic section
stim = h.IClamp (0.5 , sec = pre )
stim.amp = 10.0  #in nA
stim.delay = 5.0 #in ms
stim.dur = 5.0

# create a synapse in the pre - synaptic section
syn = h.ExpSyn(0.5,sec = post )

# connect the pre - synaptic section to the
# synapse object

nc=h.NetCon ( pre (0.5)._ref_v , syn )
nc.weight[0]=2.0

vec={}
for var in 'v_pre' , 'v_post' , 'i_syn' , 't' :
	vec[var]=h.Vector()

# record the membrane potentials and
# synaptic currents
vec['v_pre'].record(pre(0.5)._ref_v)
vec['v_post'].record(post(0.5)._ref_v)
vec['i_syn'].record(syn._ref_i)
vec['t'].record(h._ref_t)

# run the simulation
h.load_file("stdrun.hoc")
h.init()
h.tstop = 20.0
h.run()

# plot the results
import pylab
pylab.subplot(2 ,1 ,1)
pylab.plot(vec['t'] , vec['v_pre'], vec['t'] , vec['v_post'])
pylab.subplot (2 ,1 ,2)
pylab.plot(vec['t'],vec['i_syn'])
pylab.show()



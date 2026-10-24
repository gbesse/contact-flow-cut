import unittest,itertools
from contact_flow_cut import run
class Tests(unittest.TestCase):
 def setup_data(self):return {'sites':[{'id':s,'buffer_bytes':20}for s in ['A','B','D']],'source':'A','target':'D','bytes':9,'contacts':[{'id':'a','from':'A','to':'B','start':0,'end':1,'capacity_bytes':7},{'id':'b','from':'B','to':'D','start':1,'end':2,'capacity_bytes':5}]}
 def test_bottleneck_has_equal_cut(self):
  r=run(self.setup_data());self.assertEqual(r['delivered_bytes'],5);self.assertEqual(r['min_cut_bytes'],5)
 def test_buffer_binds_waiting_not_instant_handoff(self):
  d=self.setup_data();d['sites'][1]['buffer_bytes']=0;self.assertEqual(run(d)['delivered_bytes'],5);d['contacts'][1]['start']=2;d['contacts'][1]['end']=3;self.assertEqual(run(d)['delivered_bytes'],0)
 def test_parallel_direct_paths_against_independent_capacity_formula(self):
  for a,b in itertools.product(range(4),repeat=2):
   d=self.setup_data();d['contacts']=[{'id':str(i),'from':'A','to':'D','start':0,'end':1,'capacity_bytes':v}for i,v in enumerate((a,b))];r=run(d);self.assertEqual(r['delivered_bytes'],min(9,a+b));self.assertEqual(r['min_cut_bytes'],r['delivered_bytes'])
 def test_unreachable_and_same_site(self):
  d=self.setup_data();d['contacts']=[];self.assertEqual(run(d)['delivered_bytes'],0);d['target']='A';self.assertEqual(run(d)['delivered_bytes'],9)
 def test_backward_time_rejected(self):
  d=self.setup_data();d['contacts'][0]['end']=0
  with self.assertRaises(ValueError):run(d)

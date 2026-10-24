from collections import deque
from .common import integer,identifier,unique_ids

def run(data):
 sites=data['sites'];contacts=data['contacts'];unique_ids(sites);unique_ids(contacts)
 if not 1<=len(sites)<=20 or len(contacts)>100:raise ValueError('bounds')
 caps={r['id']:integer(r['buffer_bytes'],0,1000000)for r in sites};source=identifier(data['source']);target=identifier(data['target']);supply=integer(data['bytes'],0,1000000)
 if source not in caps or target not in caps:raise ValueError('endpoint')
 times={0}
 for c in contacts:
  if c['from']not in caps or c['to']not in caps:raise ValueError('endpoint')
  a=integer(c['start'],0,1000000);z=integer(c['end'],a+1,1000001);integer(c['capacity_bytes'],0,1000000);times.update((a,z))
 times=sorted(times);nodes={(site,t):i for i,(site,t)in enumerate((s,t)for s in caps for t in times)};S=len(nodes);T=S+1;adj=[[]for _ in range(T+1)];original=[]
 def edge(u,v,cap,kind,label):
  index=len(adj[u]);adj[u].append([v,len(adj[v]),cap]);adj[v].append([u,index,0]);original.append((u,index,cap,kind,label))
 edge(S,nodes[source,0],supply,'supply',source)
 for site in caps:
  for a,z in zip(times,times[1:]):edge(nodes[site,a],nodes[site,z],caps[site],'buffer',{'site':site,'start':a,'end':z})
 for c in contacts:edge(nodes[c['from'],c['start']],nodes[c['to'],c['end']],c['capacity_bytes'],'contact',c['id'])
 for t in times:edge(nodes[target,t],T,supply,'delivery',t)
 total=0
 while True:
  parent={S:None};q=deque([S])
  while q and T not in parent:
   u=q.popleft()
   for i,e in enumerate(adj[u]):
    if e[2]>0 and e[0]not in parent:parent[e[0]]=(u,i);q.append(e[0])
  if T not in parent:break
  amount=supply;v=T
  while v!=S:u,i=parent[v];amount=min(amount,adj[u][i][2]);v=u
  v=T
  while v!=S:u,i=parent[v];e=adj[u][i];e[2]-=amount;adj[v][e[1]][2]+=amount;v=u
  total+=amount
 reach={S};q=deque([S])
 while q:
  for v,_,cap in adj[q.popleft()]:
   if cap>0 and v not in reach:reach.add(v);q.append(v)
 cut=[{'kind':kind,'label':label,'capacity_bytes':cap}for u,i,cap,kind,label in original if u in reach and adj[u][i][0]not in reach]
 flows=[{'contact':label,'bytes':cap-adj[u][i][2]}for u,i,cap,kind,label in original if kind=='contact']
 return {'delivered_bytes':total,'undelivered_bytes':supply-total,'min_cut_bytes':sum(x['capacity_bytes']for x in cut),'cut':cut,'contact_flows':flows,'time_nodes':len(nodes),'model':'integer_byte_flow_fixed_contacts_zero_time_handoff'}

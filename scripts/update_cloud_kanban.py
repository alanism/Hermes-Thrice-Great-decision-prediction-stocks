"""Update durable acceptance board. Only evidence-backed Done counts."""
import argparse
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'docs/cloud-portability'

def render(data):
 done=sum(t['status']=='Done' for t in data['tasks']);total=len(data['tasks'])
 columns=''.join('<section><h2>'+status+'</h2>'+''.join('<article><b>'+escape(t['task'])+'</b><p>'+escape(t['evidence'] or 'Evidence pending')+'</p></article>' for t in data['tasks'] if t['status']==status)+'</section>' for status in ['To do','In progress','Blocked','Done'])
 return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Portable cloud implementation progress</title><style>body{font:17px system-ui;background:#f7f4ec;color:#202723;margin:2rem}progress{width:100%;height:2rem}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}article{background:white;padding:1rem;border:1px solid #ccc;margin-bottom:1rem}p{line-height:1.5}</style><h1>Decision ≥ Prediction · Portable cloud build</h1><p>'+str(done)+' / '+str(total)+' acceptance tasks complete ('+str(round(100*done/total))+'%). In-progress work is not counted as complete.</p><progress aria-label="Completed acceptance tasks" value="'+str(done)+'" max="'+str(total)+'">'+str(done)+'/'+str(total)+'</progress><p>Updated: '+escape(data['updated_at'])+'</p><p>Next: '+escape(data['next_action'])+'</p><main>'+columns+'</main><p>This board records implementation progress, not live market, browser or native host acceptance.</p></html>'

def main():
 p=argparse.ArgumentParser();p.add_argument('--task',type=int,required=True);p.add_argument('--status',choices=['To do','In progress','Blocked','Done'],required=True);p.add_argument('--evidence',required=True);p.add_argument('--next',required=True);a=p.parse_args()
 data=json.loads((ROOT/'tasks.json').read_text());task=next(t for t in data['tasks'] if t['id']==a.task)
 if a.status=='Done' and not a.evidence.strip(): raise ValueError('Done requires evidence')
 task.update(status=a.status,evidence=a.evidence);data['updated_at']=datetime.now(timezone.utc).isoformat();data['next_action']=a.next
 (ROOT/'tasks.json').write_text(json.dumps(data,indent=2)+'\n');(ROOT/'KANBAN.html').write_text(render(data))
if __name__=='__main__':main()

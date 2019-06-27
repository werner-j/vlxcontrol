import subprocess,asyncio,json,time,argparse
from bottle import run, post, request, response, get, route
from pyvlx import Position, PyVLX

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")
args = parser.parse_args()

host = args.host
port = int(args.port)

async def main(loop):
    print('Starting Control Server for KLF200...')
    global pyvlx
    pyvlx = PyVLX('pyvlx.yaml', loop=loop)
    await pyvlx.load_nodes()

if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(main(LOOP))

async def set(node,pos):
    await pyvlx.nodes[node].set_position(Position(position_percent=pos),wait_for_completion=False)

@route('/set',method = 'POST')
def process():
    reqType = request.content_type
    if (reqType != 'application/json'):
        return('{ "result" : "fail", "reason" : "unsupported request type" }')

    length = int(request.content_length)
    message = json.load(request.body)

    try:
        NODE = message['node']
        POS = message['position']
    except:
        return('{ "result" : "fail", "reason" : "node or position not provided" }')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(set(NODE,POS))

    return('{ "result" : "ok", "node" : "',NODE,'", "position" : "',str(POS),'" }')

run(host=host, port=port, debug=True)


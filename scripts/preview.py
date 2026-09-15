"""Local preview with support for video Range requests."""
import argparse
from functools import partial
from performance_audit import Handler, ROOT, ThreadingHTTPServer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    with ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=str(ROOT))) as server:
        print(f'Preview: http://127.0.0.1:{args.port}/ko/index.html', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

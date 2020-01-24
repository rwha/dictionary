#!/usr/bin/env python
import re
import sys
import zlib
from collections import defaultdict
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path


def iter_words(filepath):
    WORD_LINE = re.compile(r"^[A-Z]+-?$")
    with open(filepath) as fp:
        for line in fp:
            if WORD_LINE.match(line):
                yield True, line.strip()
            else:
                yield False, line.strip()


def load_from_file(filepath):
    sys.stdout.write(f"parsing {filepath}... ")
    sys.stdout.flush()
    book = {}
    word = None
    defn = []
    for new_word, line in iter_words(filepath):
        if new_word:
            book[word] = zlib.compress(bytes("\n".join(defn), "utf-8"))
            word = line.lower()
            defn.clear()
        if word:
            defn.append(line)
    sys.stdout.write("finished.\n")
    sys.stdout.flush()
    return book


class Responder(BaseHTTPRequestHandler):

    book = load_from_file(str((Path(__file__).parent / "dictionary.txt").resolve()))

    def _set_headers(self, response=200):
        self.send_response(response)
        self.send_header("Content-Type", "text/plain; charset=UTF-8")
        self.end_headers()

    def _html(self, msg):
        return zlib.decompress(msg)

    def do_GET(self):
        word = self.path.split("/")[-1].lower()
        if word and word in self.book:
            self._set_headers()
            self.wfile.write(self._html(self.book[word]))
        else:
            self._set_headers(response=404)
            self.wfile.write(self._html([f"{word} not found"]))
        self.close_connection = True
        sys.stderr.flush()


def run(server=HTTPServer, handler=Responder, address="0.0.0.0", port=1913):
    s = (address, port)
    httpd = server(s, handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stdout.write("quitting...")
    except Exception as e:
        sys.stdout.write("exiting:" + repr(e))
    finally:
        httpd.shutdown()
        sys.stdout.flush()
        sys.stderr.flush()


if __name__ == "__main__":
    run()

#!/usr/bin/env python
import re
import sys
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
    for new_word, line in iter_words(filepath):
        if new_word:
            word = line.lower()
            book.setdefault(word, [])
        else:
            if word:
                book[word].append(line)

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
        return msg.encode("utf8")

    def do_GET(self):
        word = self.path.split("/")[-1].lower()
        if word and word in self.book:
            self._set_headers()
            self.wfile.write(self._html("\n".join(self.book[word])))
        else:
            self._set_headers(response=404)
            self.wfile.write(self._html(f"{word} not found\n"))
        self.close_connection = True
        sys.stderr.flush()


def run(server=HTTPServer, handler=Responder, address="127.0.0.1", port=1913):
    s = (address, port)
    httpd = server(s, handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stdout.write("exiting...")
        httpd.shutdown()
        sys.stdout.write("cleanly exited")
    except Exception as e:
        sys.stdout.write("exiting:", str(e))
        httpd.shutdown()


if __name__ == "__main__":
    run()

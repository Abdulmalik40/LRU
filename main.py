import sys
from collections import OrderedDict, deque

cap = 0
lru = OrderedDict(); fifo = deque(); fifo_set = set(); lfu = {}; lfu_freq = {}
lru_h = fifo_h = lfu_h = 0
out = []

for raw in sys.stdin:
    line = raw.rstrip("\n")
    if not line: continue
    parts = line.split()
    cmd = parts[0]
    if cmd == "CAP":
        cap = int(parts[1])
    elif cmd == "ACCESS":
        k = parts[1]
        # TODO: update all three caches for this access, on the same key `k`.
        # - LRU (`lru`, an OrderedDict): hit if k already present (move it to
        #   the MRU end, count in lru_h); else miss -> insert k, evicting the
        #   least-recently-used entry first if at capacity (`cap`).
        # - FIFO (`fifo` deque + `fifo_set`): hit if k already present (count
        #   in fifo_h); else miss -> append k, evicting the oldest-inserted
        #   entry first if at capacity.
        # - LFU (`lfu` + `lfu_freq`): hit if k already present (bump its
        #   frequency, count in lfu_h); else miss -> insert with frequency 1,
        #   evicting the lowest-frequency entry first if at capacity.
        pass
    elif cmd == "STATS":
        out.append(f"lru_hits={lru_h} fifo_hits={fifo_h} lfu_hits={lfu_h}")

print("\n".join(out))

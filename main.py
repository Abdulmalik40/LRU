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
        if cap <= 0:
            continue

        # ---- LRU ----
        if k in lru:
            lru.move_to_end(k)
            lru_h += 1
        else:
            if len(lru) >= cap:
                lru.popitem(last=False)
            lru[k] = None

        # ---- FIFO ----
        if k in fifo_set:
            fifo_h += 1
        else:
            if len(fifo) >= cap:
                old = fifo.popleft()
                fifo_set.discard(old)
            fifo.append(k)
            fifo_set.add(k)

        # ---- LFU ----
        if k in lfu:
            f = lfu[k]
            lfu_freq[f].discard(k)
            if not lfu_freq[f]:
                del lfu_freq[f]
            lfu[k] = f + 1
            lfu_freq.setdefault(f + 1, set()).add(k)
            lfu_h += 1
        else:
            if len(lfu) >= cap:
                min_f = min(lfu_freq)
                victim = next(iter(lfu_freq[min_f]))
                lfu_freq[min_f].discard(victim)
                if not lfu_freq[min_f]:
                    del lfu_freq[min_f]
                del lfu[victim]
            lfu[k] = 1
            lfu_freq.setdefault(1, set()).add(k)
    elif cmd == "STATS":
        out.append(f"lru_hits={lru_h} fifo_hits={fifo_h} lfu_hits={lfu_h}")

print("\n".join(out))
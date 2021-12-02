# import random
#
# while True:
#     a, b, c, d = (random.randrange(1, 30) for _ in range(4))
#     e = random.randrange(1, 40)
#     # print(f"{a ** 5} + {b ** 5} + {c ** 5} + {d ** 5} != {e ** 5}")
#     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#         print(f"{a ** 5} + {b ** 5} + {c ** 5} + {d ** 5} = {e ** 5}")
#         exit()

import time
start_time = time.perf_counter()
for a in range(1, 151):
    # print(a)
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                total = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(total ** (1/5))
                # print(f"{a} ** 5 + {b} ** 5 + {c} ** 5 + {d} ** 5 != {e} ** 5")
                if total == e ** 5:
                    end_time = time.perf_counter()
                    print(f"{a} ** 5 + {b} ** 5 + {c} ** 5 + {d} ** 5 = {e} ** 5")
                    print(f"Elapsed time: {end_time - start_time}")
                    exit()

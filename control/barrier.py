import time
from misc.consts import DEBUG_MODE

if not DEBUG_MODE:
    from control.gpio import GPIO

    gpio = GPIO()


class BarrierClass:

    def __init__(self):
        self._open = 'Open Barrier'

    def open(self, req_json: dict):
        if req_json:
            for key in req_json:
                if req_json[key] == "ALLOW":
                    # OPEN BARRIER
                    if not DEBUG_MODE:
                        gpio.open_barrier()
                    else:
                        print(f"OPENING BARRIER for {key}")
                    break

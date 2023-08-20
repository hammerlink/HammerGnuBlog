from gnuradio import gr
from datetime import datetime
# import pika


class SignalWatch(gr.sync_block):
    def __init__(self, exchange_name, routing_key, host='localhost', port=5672):
        gr.sync_block.__init__(self,
            name="SignalWatch",
            in_sig=[],
            out_sig=[])


    def work(self, input_items, output_items):
        print("----- test", datetime.now())

        return len(input_items[0])
